#!/usr/bin/env python3

import tkinter as tk

class Calculadora:
    def __init__(self, master) -> None:
        # Initialize the calculator with the main window (master)
        self.master = master
        # Create an entry widget for the display of the calculator with right text justification
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#6495DE", justify="right")
        # Place the display at row 0, column 0, spanning 4 columns in the main window's grid layout
        self.display.grid(row=0, column=0, columnspan=4)

        # Initial positions for buttons
        row = 1
        col = 0

        # List of buttons to be added to the calculator
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", 
            "="
        ]

        # Loop through the list of buttons to create and place them in the grid
        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            # Move to the next row after every 4 buttons
            if col > 3:
                col = 0
                row += 1

    def clear_display(self):
        # Clear the display entry widget
        self.display.delete(0, "end")

    def calculate(self):
        # Placeholder for calculation method (not yet implemented)
        print(f"\n[+] Este metodo aun no ha sido implementado")

    def click(self):
        # Placeholder for click method
        pass

    def build_button(self, button, row, col):
        # Create buttons with specific commands for 'C' and '=' buttons, and a generic command for others
        if button == "C":
            b = tk.Button(self.master, text=button, width=3, command=self.clear_display)
        elif button == "=":
            b = tk.Button(self.master, text=button, width=3, command=self.calculate)
        else:
            b = tk.Button(self.master, text=button, width=3, command=self.click)
        
        # Place the button in the specified row and column of the grid
        b.grid(row=row, column=col)

# Create the main window instance
root = tk.Tk()
# Create an instance of the Calculadora class with the main window as the master
my_gui = Calculadora(root)
# Start the Tkinter event loop to run the application
root.mainloop()