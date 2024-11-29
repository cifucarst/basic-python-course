#!/usr/bin/env python3


import tkinter as tk


root = tk.Tk()
root.geometry("300x200")
root.title("Frame() Widget")

# Create a Frame widget with a blue background and a border width of 5 pixels
frame = tk.Frame(root, bg="blue", bd=5)

# Place the frame in the center of the main window using relative positioning
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a Label widget with a green background and specified text, inside the frame
label = tk.Label(frame, text="This is a test label", bg="green")

# Create another Label widget with a red background and specified text, inside the frame
label1 = tk.Label(frame, text="This is a second test label", bg="red")

# Pack the first label into the frame and allow it to expand horizontally
label.pack(fill=tk.X)

# Pack the second label into the frame and allow it to expand horizontally
label1.pack(fill=tk.X)

root.mainloop()