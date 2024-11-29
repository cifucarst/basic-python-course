#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry("200x70")

# Define a function to be called when the button is pressed
def open_file():
    # Open a file dialog and store the selected file path
    file_route = filedialog.askopenfilename()
    # Print the selected file path to the console
    print(f"\n[+] The file route: {file_route}")

# Create a Button widget with specified text and action on click
boton = tk.Button(root, text="open file", command=open_file)

# Pack the button into the main window with padding on the y-axis
boton.pack(pady=15)

root.mainloop()