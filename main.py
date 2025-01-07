from customtkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy
import sqlite3
import requests
import time

conn = sqlite3.connect('portfolio.db')

def main():
    root = CTk()
    root.title("Crypto Visualizer")
    root.geometry("400x300")

    addBtn = CTkButton(master=root, text="Add New Crypto", command=lambda: subWindow(root, 1)).pack(pady=10)
    updateBtn = CTkButton(master=root, text="Update", command=lambda: subWindow(root, 2)).pack(pady=10)
    removeBtn = CTkButton(master=root, text="Remove", command=lambda: subWindow(root, 3)).pack(pady=10)
    pieBtn = CTkButton(master=root, text="Make Pie Chart", command=lambda: displayGraphs(root, 1)).pack(pady=10)
    lineBtn = CTkButton(master=root, text="Make Linegraph", command=lambda: displayGraphs(root, 2)).pack(pady=10)
    priceBtn = CTkButton(master=root, text="Update Prices", command=lambda: updatePrice()).pack(pady=10)

    root.mainloop()

def displayGraphs(root, index):
    if index == 1:
        # Create a new subwindow for the pie chart
        pieWin = CTkToplevel(master=root)
        pieWin.title("Pie Chart")
        pieWin.geometry("800x600")  # Larger subwindow

        # Create a frame within the subwindow for the chart
        frame = CTkFrame(pieWin)
        frame.pack(fill='both', expand=True, padx=20, pady=20)  # Use the entire window space

        # Directly create the pie chart in the subwindow
        pieChart(pieWin, frame)

    elif index == 2:
        print("Not ready yet : )")

def destroyWin(root, subWin):
    subWin.destroy()
    root.deiconify()

def getPrices(crypto):
    print(f"checjing {crypto}")
    cryptoStr = ','.join(crypto)

    apiKey = f"https://api.coingecko.com/api/v3/simple/price?ids={cryptoStr}&vs_currencies=usd"

    response = requests.get(apiKey)
    data = response.json()

    if crypto in data:
        print(data[crypto]["usd"])
        return data[crypto]["usd"]
    
    if response.status_code == 429:
        print("Rate limit exceeded. Sleeping for 60 seconds...")
        time.sleep(60)  # Sleep for 60 seconds before retrying
        response = requests.get(apiKey)  # Retry the request

        return data[crypto]["usd"]
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")

def updatePrice():
    data = readData()

    for crypto in data:
        print (crypto[2])
        cryptoId = crypto[2].lower()
        price = getPrices(cryptoId)

        if price is not None:
            # Update the price for each cryptocurrency in the database
            conn.execute("UPDATE portfolio SET pricegdp = ? WHERE crypto = ?", (price, crypto[0]))
            conn.commit()

def pieChart(pieWin, frame):
    data = readData()

    labels = [row[0] for row in data]
    sizes = [row[3] for row in data]
    #colors = []

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis("equal")

    pieCanvas = FigureCanvasTkAgg(fig, master=frame)  # Embed the chart into the frame
    pieCanvas.draw()
    pieCanvas.get_tk_widget().pack(fill='both', expand=True)

def lineGraph():
    return

def subWindow(root, index):
    cryptoName = StringVar()
    amount = StringVar()
    value = StringVar()

    root.withdraw()

    if index == 1:
        addWin = CTkToplevel(master=root)
        addWin.title("Add New Crypto")
        addWin.geometry("300x300")

        coinEntry = CTkEntry(master=addWin, placeholder_text="Enter the name of the Crypto", textvariable=cryptoName).pack(pady=10)
        amountEntry = CTkEntry(master=addWin, placeholder_text="How much are you adding?", textvariable=amount).pack(pady=10)
        valueEntry = CTkEntry(master=addWin, placeholder_text="What is its current value?", textvariable=value).pack(pady=10)

        enterBtn = CTkButton(master=addWin, text="Enter", command=lambda: addData(cryptoName.get(), amount.get(), value.get(), root, addWin)).pack(pady=10)

    elif index == 2:
        upWin = CTkToplevel(master=root)
        upWin.title("Update Crypto")
        upWin.geometry("300x300")

        coinEntry = CTkEntry(master=upWin, placeholder_text="Enter the name of the Crypto", textvariable=cryptoName).pack(pady=10)
        amountEntry = CTkEntry(master=upWin, placeholder_text="How much are you adding?", textvariable=amount).pack(pady=10)
        valueEntry = CTkEntry(master=upWin, placeholder_text="What is its current value?", textvariable=value).pack(pady=10)

        enterBtn = CTkButton(master=upWin, text="Enter", command=lambda: updateData(cryptoName.get(), amount.get(), value.get(), root, upWin)).pack(pady=10)
    
    elif index == 3:
        delWin = CTkToplevel(master=root)
        delWin.title("Remove Crypto")
        delWin.geometry("300x300")

        coinEntry = CTkEntry(master=delWin, placeholder_text="Enter the name of the Crypto", textvariable=cryptoName).pack(pady=10)

        enterBtn = CTkButton(master=delWin, text="Enter", command=lambda: delData(cryptoName.get(), root, delWin)).pack(pady=10)

def addData(crypto, amount, val, root, addWin):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolio (
        id INTEGER PRIMARY KEY,
        crypto TEXT,
        amount INTEGER,
        value INTEGER
    )
    ''')

    #Check if crypto being added exists in DB
    cursor.execute('SELECT * FROM portfolio WHERE crypto = ?', (crypto,))
    exists = cursor.fetchone()

    if exists:
        print(f"{crypto} already exists")
    
    else:
        try:
            cursor.execute('''
                INSERT INTO portfolio (crypto, amount, value) VALUES (?, ?, ?)
                ''', (crypto, amount, val))
            
            conn.commit()

        except Exception as e:
            print(f"Error {e}")

    destroyWin(root, addWin)

def updateData(crypto, amount, val, root, upWin):
    try: 
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM portfolio WHERE crypto = ?", (crypto,))
        existing = cursor.fetchone()

        if existing:
            if amount == "":
                cursor.execute('''
                UPDATE portfolio
                SET value = ?
                WHERE crypto = ?
            ''', (val, crypto))
                
            elif val == "":
                cursor.execute('''
                UPDATE portfolio
                SET amount = ?,
                WHERE crypto = ?
            ''', (amount, crypto))

            else:
                cursor.execute('''
                UPDATE portfolio
                SET amount = ?, value = ?
                WHERE crypto = ?
            ''', (amount, val, crypto))

            conn.commit()

    except Exception as e:
        print("Error, {e}")

    destroyWin(root, upWin)

def readData():
    cursor = conn.cursor()

    cursor.execute('''
        SELECT crypto, amount, value FROM portfolio
    ''')

    data = cursor.fetchall()

    return data

def delData(crypto, root, delWin):
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM portfolio WHERE crypto = ?', (crypto,))
        conn.commit()

    except Exception as e:
        print(f"Error, {e}")

        delWin = CTkToplevel(master=root)
        delWin.title("Remove Crypto")
        delWin.geometry("300x300")

        coinEntry = CTkEntry(master=delWin, placeholder_text="Enter the name of the Crypto", textvariable=crypto).pack(pady=10)

        enterBtn = CTkButton(master=delWin, text="Enter", command=lambda: delData(crypto.get())).pack(pady=10)

        destroyWin(root, delWin)

if __name__ == "__main__":
   main()