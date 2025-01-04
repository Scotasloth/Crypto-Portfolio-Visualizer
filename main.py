from customtkinter import *
import matplotlib
import numpy
import sqlite3

conn = sqlite3.connect('portfolio.db')

def main():
    root = CTk()
    root.title("Crypto Visualizer")
    root.geometry("400x300")

    addBtn = CTkButton(master=root, text="Add New Crypto", command=lambda: addData(root)).pack(pady=10)
    updateBtn = CTkButton(master=root, text="Update", command=lambda: updateData(root)).pack(pady=10)
    removeBtn = CTkButton(master=root, text="Remove", command=lambda: delData(root)).pack(pady=10)
    pieBtn = CTkButton(master=root, text="Make Pie Chart", command=lambda: pieChart()).pack(pady=10)
    lineBtn = CTkButton(master=root, text="Make Linegraph", command=lambda: lineGraph()).pack(pady=10)

    root.mainloop()

def pieChart():
    return

def lineGraph():
    return

def addData(root):
    addWin = CTkToplevel(master=root)
    addWin.title("Add New Crypto")
    addWin.geometry("300x300")

    coinEntry = CTkEntry(master=addWin, placeholder_text="Enter the name of the Crypto").pack(pady=10)
    amountEntry = CTkEntry(master=addWin, placeholder_text="How much are you adding?").pack(pady=10)
    valueEntry = CTkEntry(master=addWin, placeholder_text="What is its current value?").pack(pady=10)

    enterBtn = CTkButton(master=addWin, text="Enter").pack(pady=10)

def updateData(root):
    upWin = CTkToplevel(master=root)
    upWin.title("Update Crypto")
    upWin.geometry("300x300")

    coinEntry = CTkEntry(master=upWin, placeholder_text="Enter the name of the Crypto").pack(pady=10)
    amountEntry = CTkEntry(master=upWin, placeholder_text="How much are you adding?").pack(pady=10)
    valueEntry = CTkEntry(master=upWin, placeholder_text="What is its current value?").pack(pady=10)

    enterBtn = CTkButton(master=upWin, text="Enter").pack(pady=10)

def readData():
    return

def delData(root):
    delWin = CTkToplevel(master=root)
    delWin.title("Remove Crypto")
    delWin.geometry("300x300")

    coinEntry = CTkEntry(master=delWin, placeholder_text="Enter the name of the Crypto")

    enterBtn = CTkButton(master=delWin, text="Enter").pack(pady=10)

if __name__ == "__main__":
   main()