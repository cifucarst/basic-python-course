#!/usr/bin/env python3

import tkinter as tk

class Calculadora:
    def __init__(self, master) -> None:
        # Initialize the calculator with the main window (master)
        self.master = master
        # Create an entry widget for the display of the calculator
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#6495DE")
        # Place the display at row 0, column 0 in the main window's grid layout
        self.display.grid(row=0, column=0)

# Create the main window instance
root = tk.Tk()
# Create an instance of the Calculadora class with the main window as the master
my_gui = Calculadora(root)
# Start the Tkinter event loop to run the application
root.mainloop()