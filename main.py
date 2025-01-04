from customtkinter import *
import matplotlib
import numpy
import sqlite3

def main():
    root = CTk()
    root.title("Crypto Visualizer")
    root.geometry("400x300")

    addBtn = CTkButton(master=root, text="Add New Crypto", command=lambda: addData()).pack(pady=10)
    updateBtn = CTkButton(master=root, text="Update", command=lambda: updateData()).pack(pady=10)
    removeBtn = CTkButton(master=root, text="Remove", command=lambda: delData()).pack(pady=10)
    pieBtn = CTkButton(master=root, text="Make Pie Chart", command=lambda: pieChart()).pack(pady=10)
    lineBtn = CTkButton(master=root, text="Make Linegraph", command=lambda: lineGraph()).pack(pady=10)

    root.mainloop()

def pieChart():
    return

def lineGraph():
    return

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