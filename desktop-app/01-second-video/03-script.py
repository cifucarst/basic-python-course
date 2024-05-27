#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

root.geometry("700x550")
# Set the size of the main window to 700 pixels wide by 550 pixels tall.

root.title("Text() Widget")
# Set the title of the main window to "Text() Widget".

def get_data():
    data = test_widget.get("1.0", tk.END)
    print(f"\n[+] Data from the user:\n\n {data}")
# Define a function named 'get_data' that retrieves the text from the Text widget 'test_widget'.
# The method get("1.0", tk.END) retrieves all text from the Text widget starting from the first character ("1.0") to the end (tk.END).
# Print the retrieved data to the console.

test_widget = tk.Text(root)
# Create a Text widget with the parent 'root'. This widget allows the user to enter and edit multiple lines of text.

test_widget.pack(pady=5, padx=15, fill=tk.X)
# Pack the Text widget into the root window.
# pady=5 adds a vertical padding of 5 pixels above and below the widget.
# padx=15 adds a horizontal padding of 15 pixels to the left and right of the widget.
# fill=tk.X makes the Text widget expand horizontally to fill the available space.

button = tk.Button(root, text="Get data", command=get_data)
# Create a Button widget with the parent 'root', the text "Get data", and set its command to the 'get_data' function.
# This means that when the button is pressed, the 'get_data' function will be called.

button.pack()
# Pack the Button widget into the root window.

root.mainloop()