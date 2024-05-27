#!/usr/bin/env python3
# This line is called a shebang and tells the operating system to use the Python 3 interpreter to run this script.

import tkinter as tk
# Import the tkinter module, which provides tools for creating graphical user interfaces (GUIs) in Python.

root = tk.Tk()
# Create the main window (also known as the root window) of the GUI application.

root.title("Grid Method")
# Set the title of the main window to "Grid Method".

label1 = tk.Label(root, text="My first label", bg="yellow")
# Create a Label widget with the parent 'root', the text "My first label", and a yellow background.

label2 = tk.Label(root, text="My second label", bg="blue")
# Create a Label widget with the parent 'root', the text "My second label", and a blue background.

label3 = tk.Label(root, text="My third label", bg="red")
# Create a Label widget with the parent 'root', the text "My third label", and a red background.

label1.place(x=20, y=20)
# Place the first label widget at an absolute position (20, 20) pixels from the top-left corner of the root window.

label2.place(relx=0.8, rely=0.2)
# Place the second label widget at a position relative to the size of the root window.
# relx=0.8 means 80% of the width from the left, and rely=0.2 means 20% of the height from the top.

label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# Place the third label widget at the center of the root window.
# relx=0.5 means 50% of the width from the left, and rely=0.5 means 50% of the height from the top.
# anchor=tk.CENTER ensures the label is centered at this position.

root.mainloop()
# Start the Tkinter event loop. This method listens for events such as button clicks and keeps the window open.