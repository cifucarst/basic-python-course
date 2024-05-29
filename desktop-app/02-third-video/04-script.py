#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("200x70")

# Define a function to be called when the button is pressed
def action():
    # Show an informational message box with a specified title and message
    messagebox.showinfo("Menu", "You've hit on me")

# Create a Button widget with specified text and action on click
boton = tk.Button(root, text="Press me", command=action)

# Pack the button into the main window with padding on the y-axis
boton.pack(pady=15)

root.mainloop()