#!/usr/bin/env python3

import tkinter as tk


def button_action():
    print("The button has been pressed")
# Define a function named 'button_action' that prints a message when called. 
# This function will be used as the callback for the button.

root = tk.Tk()

button = tk.Button(root, text="Click me, please", command=button_action)
# Create a Button widget with the parent 'root', the text "Click me, please", 
# and set the 'command' parameter to the 'button_action' function.
# This means that when the button is pressed, the 'button_action' function will 
# be called.

button.pack()
# Pack the button widget into the root window. The pack() method organizes widgets 
# in blocks before placing them in the parent widget.

root.mainloop()