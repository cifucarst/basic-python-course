#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello world!")
# Create a Label widget with the parent 'root' and the text "Hello world!".

label.pack()
# Pack the label widget into the root window. The pack() method organizes widgets in blocks before placing them in the parent widget.

root.mainloop()