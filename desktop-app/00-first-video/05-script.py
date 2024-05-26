#!/usr/bin/env python3

import tkinter as tk

# grid() 
# grid() - Organizes widgets in a table-like structure.


root = tk.Tk()

root.title("Grid method()")
# Set the title of the main window to "Grid method()".

label1 = tk.Label(root, text="My first label", bg="red")
# Create a Label widget with the parent 'root', the text "My first label", and a red background.

label2 = tk.Label(root, text="My second label", bg="blue")
# Create a Label widget with the parent 'root', the text "My second label", and a blue background.

label3 = tk.Label(root, text="My third label", bg="green")
# Create a Label widget with the parent 'root', the text "My third label", and a green background.

label1.grid(row=0, column=0)
# Place the first label widget in the grid at row 0, column 0.

label2.grid(row=0, column=1)
# Place the second label widget in the grid at row 0, column 1.

label3.grid(row=1, column=0, columnspan=2)
# Place the third label widget in the grid at row 1, spanning across 2 columns (columnspan=2).

root.mainloop()