#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

root.geometry("800x700")
# Set the size of the main window to 800 pixels wide by 700 pixels tall.

root.title("Entry() Widget")

entry_widget = tk.Entry(root)
# Create an Entry widget with the parent 'root'. This widget allows the user to enter a single line of text.

entry_widget.pack(pady=5, padx=5, fill=tk.X)
# Pack the Entry widget into the root window.
# pady=5 adds a vertical padding of 5 pixels above and below the widget.
# padx=5 adds a horizontal padding of 5 pixels to the left and right of the widget.
# fill=tk.X makes the Entry widget expand horizontally to fill the available space.

root.mainloop()