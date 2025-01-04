from customtkinter import *
import matplotlib
import numpy
import sqlite3

conn = sqlite3.connect('portfolio.db')

def main():
    root = CTk()
    root.title("Crypto Visualizer")
    root.geometry("400x300")

    addBtn = CTkButton(master=root, text="Add New Crypto", command=lambda: subWindow(root, 1)).pack(pady=10)
    updateBtn = CTkButton(master=root, text="Update", command=lambda: subWindow(root, 2)).pack(pady=10)
    removeBtn = CTkButton(master=root, text="Remove", command=lambda: subWindow(root, 3)).pack(pady=10)
    pieBtn = CTkButton(master=root, text="Make Pie Chart", command=lambda: pieChart()).pack(pady=10)
    lineBtn = CTkButton(master=root, text="Make Linegraph", command=lambda: lineGraph()).pack(pady=10)

    root.mainloop()

def pieChart():
    return

def lineGraph():
    return

def subWindow(root, index):
    cryptoName = StringVar()
    amount = StringVar()
    value = StringVar()

    if index == 1:
        addWin = CTkToplevel(master=root)
        addWin.title("Add New Crypto")
        addWin.geometry("300x300")

        coinEntry = CTkEntry(master=addWin, placeholder_text="Enter the name of the Crypto", textvariable=cryptoName).pack(pady=10)
        amountEntry = CTkEntry(master=addWin, placeholder_text="How much are you adding?", textvariable=amount).pack(pady=10)
        valueEntry = CTkEntry(master=addWin, placeholder_text="What is its current value?", textvariable=value).pack(pady=10)

        enterBtn = CTkButton(master=addWin, text="Enter").pack(pady=10)

    elif index == 2:
        upWin = CTkToplevel(master=root)
        upWin.title("Update Crypto")
        upWin.geometry("300x300")

        coinEntry = CTkEntry(master=upWin, placeholder_text="Enter the name of the Crypto", textvariable=cryptoName).pack(pady=10)
        amountEntry = CTkEntry(master=upWin, placeholder_text="How much are you adding?", textvariable=amount).pack(pady=10)
        valueEntry = CTkEntry(master=upWin, placeholder_text="What is its current value?", textvariable=value).pack(pady=10)

        enterBtn = CTkButton(master=upWin, text="Enter").pack(pady=10)
    
    elif index == 3:
        delWin = CTkToplevel(master=root)
        delWin.title("Remove Crypto")
        delWin.geometry("300x300")

        coinEntry = CTkEntry(master=delWin, placeholder_text="Enter the name of the Crypto", textvariable=cryptoName).pack(pady=10)

        enterBtn = CTkButton(master=delWin, text="Enter").pack(pady=10)

def addData():
    return

def updateData():
    return

def readData():
    return

def delData():
    return

if __name__ == "__main__":
   main()