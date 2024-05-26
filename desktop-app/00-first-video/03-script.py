#!/usr/bin/env python3

import tkinter as tk

# grid() place() pack()
# These are different geometry managers in Tkinter:
# grid() - Organizes widgets in a table-like structure.
# place() - Places widgets at an absolute position.
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

label1.pack()
# Pack the first label widget into the root window. The pack() method organizes widgets in blocks before placing them in the parent widget.

label2.pack()
# Pack the second label widget into the root window.

label3.pack()
# Pack the third label widget into the root window.

root.mainloop()