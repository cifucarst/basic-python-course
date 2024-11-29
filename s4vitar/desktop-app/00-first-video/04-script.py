#!/usr/bin/env python3

import tkinter as tk

# pack()
# pack() - Organizes widgets in blocks before placing them in the parent widget.


root = tk.Tk()

root.title("Pack method()")
# Set the title of the main window to "Pack method()".

label1 = tk.Label(root, text="My first label", bg="red")
# Create a Label widget with the parent 'root', the text "My first label", and a red background.

label2 = tk.Label(root, text="My second label", bg="blue")
# Create a Label widget with the parent 'root', the text "My second label", and a blue background.

label3 = tk.Label(root, text="My third label", bg="green")
# Create a Label widget with the parent 'root', the text "My third label", and a green background.

label1.pack(fill=tk.X)
# Pack the first label widget into the root window, and make it expand horizontally to fill the available space (fill=tk.X).

label2.pack(fill=tk.X)
# Pack the second label widget into the root window, and make it expand horizontally to fill the available space (fill=tk.X).

label3.pack(side=tk.BOTTOM, fill=tk.Y)
# Pack the third label widget into the root window, and place it at the bottom of the window (side=tk.BOTTOM).
# Also, make it expand vertically to fill the available space (fill=tk.Y).

root.mainloop()