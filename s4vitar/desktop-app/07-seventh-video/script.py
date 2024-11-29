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
        
        # Initialize the calculator state
        self.op_verification = False  # To verify if an operator is pressed
        self.current = ""  # To store the current number being entered
        self.op = ""  # To store the current operator
        self.total = 0  # To store the running total

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

        # Bind keyboard input to the calculator
        self.master.bind("<Key>", self.key_press)

    def key_press(self, event):
        # Handle key press events
        key = event.char
        if key == "\r":  # Enter key
            self.calculate()
            return
        elif key == "\x08":  # Backspace key
            self.clear_display()
            return
        elif key == "\x1b":  # Escape key
            self.master.quit()
            return

        # Process other key presses as button clicks
        self.click(key)

    def clear_display(self):
        # Clear the display entry widget and reset calculator state
        self.display.delete(0, "end")
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0

    def calculate(self):
        # Perform calculation based on the operator and current value
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)

        # Update the display with the result
        self.display.delete(0, "end")
        self.display.insert("end", round(self.total, 3))

    def click(self, key):
        # Handle the button click event
        if self.op_verification:
            self.op_verification = False

        # Insert the clicked button's text into the display
        self.display.insert("end", key)

        if key in "012345678" or key == ".":
            # Append number or decimal point to current input
            self.current += key
        else:
            # Handle operator input
            if self.current:
                if not self.op:
                    # Set the total if no previous operator exists
                    self.total = float(self.current)
            
            # Reset current input for the next number
            self.current = ""

            self.op_verification = True
            self.op = key

    def build_button(self, button, row, col):
        # Create buttons with specific commands for 'C' and '=' buttons, and a generic command for others
        if button == "C":
            b = tk.Button(self.master, text=button, width=3, command=lambda: self.clear_display())
        elif button == "=":
            b = tk.Button(self.master, text=button, width=3, command=lambda: self.calculate())
        else:
            b = tk.Button(self.master, text=button, width=3, command=lambda: self.click(button))
        
        # Place the button in the specified row and column of the grid
        b.grid(row=row, column=col)

# Create the main window instance
root = tk.Tk()
# Create an instance of the Calculadora class with the main window as the master
my_gui = Calculadora(root)
# Start the Tkinter event loop to run the application
root.mainloop()