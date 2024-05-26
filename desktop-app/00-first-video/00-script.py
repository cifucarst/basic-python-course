#!/usr/bin/env python3
# This line is called a shebang and tells the operating system to use the Python 3 interpreter to run 
# this script.

import tkinter as tk
# Import the tkinter module, which provides tools for creating graphical user interfaces (GUIs) in Python.

root = tk.Tk()
# Create the main window (also known as the root window) of the GUI application.

root.title("My first application")
# Set the title of the main window to "My first application".

root.mainloop()
# Start the Tkinter event loop. This method listens for events such as button clicks and keeps 
# the window open.