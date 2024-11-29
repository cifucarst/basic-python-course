#!/usr/bin/env python3

import tkinter as tk
# Import the messagebox module from tkinter for showing message boxes
from tkinter import messagebox

root = tk.Tk()
root.title("Menu() Widget")

# Define a function to be called when a menu item is selected
def menu_action():
    # Show an informational message box with a specified title and message
    messagebox.showinfo("Menu", "Everything gets better")

# Create a Menu widget to be the main menu bar of the application
bar_menu = tk.Menu(root)

# Configure the main window to use the created menu bar
root.config(menu=bar_menu)

# Create a dropdown menu (menu1) without a tear-off option
menu1 = tk.Menu(bar_menu, tearoff=0)

# Add the dropdown menu to the menu bar with the label "Menu"
bar_menu.add_cascade(label="Menu", menu=menu1)

# Add commands (menu items) to the dropdown menu
menu1.add_command(label="Option 1")
menu1.add_command(label="Option 2")

# Create another dropdown menu (menu2) without a tear-off option
menu2 = tk.Menu(bar_menu, tearoff=0)

# Add the second dropdown menu to the menu bar with the label "Extras"
bar_menu.add_cascade(label="Extras", menu=menu2)

# Add a command (menu item) to the second dropdown menu
# When this menu item is selected, the menu_action function is called
menu2.add_command(label="harder", command=menu_action)

root.mainloop()