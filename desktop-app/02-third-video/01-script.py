#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Canvas() Widget")

canvas = tk.Canvas(root, width=400, height=400, bg="white")

# Pack the canvas into the main window with padding at the top and bottom
canvas.pack(pady=15)

# Create an oval (circle/ellipse) on the canvas with specified coordinates and fill color
oval = canvas.create_oval(50, 50, 150, 150, fill="red")

# Create a rectangle on the canvas with specified coordinates and fill color
rect = canvas.create_rectangle(170, 50, 350, 100, fill="green")

# Create a line on the canvas with specified start and end coordinates, width, and color
line = canvas.create_line(50, 250, 200, 320, width=5, fill="blue")

root.mainloop()