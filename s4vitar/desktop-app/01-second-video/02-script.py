#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry("230x100")
root.title("Entry() Widget")

def get_data():
    data = entry_widget.get()
    print(f"\n[+] Data from the user: {data}")

entry_widget = tk.Entry(root)
entry_widget.pack(pady=5,padx=15,fill=tk.X)

button = tk.Button(root,text="Get data",command=get_data)
button.pack(padx=15,fill=tk.X)

root.mainloop()