#!/usr/bin/env python3

# Import the tkinter module for GUI creation
import tkinter as tk
# Import filedialog and messagebox modules from tkinter for file dialogs and message boxes
from tkinter import filedialog, messagebox

# Define a class for a simple text editor
class SimpleTextEditor:
    # Initialize the editor with the main window (root)
    def __init__(self, root) -> None:
        self.root = root
        
        # Create a Text widget for the text area
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        
        # Initialize the current open file as an empty string
        self.current_open_file = ""

    # Method to create a new file
    def new_file(self):
        # Clear the text area
        self.text_area.delete("1.0", tk.END)
        # Reset the current open file
        self.current_open_file = ""

    # Method to open an existing file
    def open_file(self):
        # Open a file dialog to select a file
        filename = filedialog.askopenfilename()

        if filename:
            # Clear the text area
            self.text_area.delete("1.0", tk.END)
            # Read the content of the selected file and insert it into the text area
            with open(filename, "r") as file:
                self.text_area.insert("1.0", file.read())
            # Update the current open file with the selected file path
            self.current_open_file = filename

    # Method to save the current file
    def save_file(self):
        # If there is no currently open file, open a save dialog to get a new file path
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename()

            if new_file_path:
                self.current_open_file = new_file_path
            else:
                return
        # Save the content of the text area to the current open file
        with open(self.current_open_file, "w") as file:
            file.write(self.text_area.get("1.0", tk.END))

    # Method to confirm and handle quitting the application
    def quit_confirm(self):
        # Show a confirmation dialog before quitting
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

# Create the main window (root) of the application
root = tk.Tk()
# Set the dimensions of the main window to 700x500 pixels
root.geometry("700x500")

# Create an instance of the SimpleTextEditor class
editor = SimpleTextEditor(root)

# Create a Menu widget to be the main menu bar of the application
menu_bar = tk.Menu(root)
# Create a dropdown menu (menu_options) without a tear-off option
menu_options = tk.Menu(menu_bar, tearoff=0)

# Add commands (menu items) to the dropdown menu with corresponding methods from the editor
menu_options.add_command(label="New", command=editor.new_file)
menu_options.add_command(label="Open", command=editor.open_file)
menu_options.add_command(label="Save", command=editor.save_file)
menu_options.add_command(label="Exit", command=editor.quit_confirm)

# Configure the main window to use the created menu bar
root.config(menu=menu_bar)
# Add the dropdown menu to the menu bar with the label "File"
menu_bar.add_cascade(label="File", menu=menu_options)

# Enter the main event loop to make the window responsive
root.mainloop()