#!/usr/bin/env python3

import ssl
import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def send_message(client_socket, username, text_widget, entry_widget):
    # Get the message from the entry widget
    message = entry_widget.get()
    
    # Send the message to the server
    client_socket.sendall(f"{username} > {message}".encode())
    
    # Clear the entry widget and display the message in the text widget
    entry_widget.delete(0, END)
    text_widget.configure(state="normal")
    text_widget.insert(END, f"{username} > {message}\n")
    text_widget.configure(state="disabled")

def receive_message(client_socket, text_widget):
    # Continuously receive messages from the server
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            # Display the received message in the text widget
            text_widget.configure(state="normal")
            text_widget.insert(END, message)
            text_widget.configure(state="disabled")

        except:
            break

def list_users_request(client_socket):
    # Send a request to list all users
    client_socket.sendall("!usuarios".encode())

def exit_request(client_socket, username, window):
    # Send a message indicating the user is leaving the chat
    client_socket.sendall(f"\n[!] User {username} has left the chat\n\n".encode())
    
    # Close the client socket and exit the application
    client_socket.close()
    window.quit()
    window.destroy()

def client_program():
    host = 'localhost'
    port = 12345

    # Create and connect the client socket using SSL
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket = ssl.wrap_socket(client_socket)
    client_socket.connect((host, port))

    # Get the username from the user
    username = input(f"\n[+] Enter your username: ")
    client_socket.sendall(username.encode())

    # Start the Tkinter GUI
    window = Tk()
    window.title("Chat")

    # Create a ScrolledText widget for displaying messages
    text_widget = ScrolledText(window, state="disabled")
    text_widget.pack(padx=5, pady=5)

    # Create a frame to hold the entry widget and send button
    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=2, fill=BOTH, expand=1)

    # Create an entry widget for typing messages
    entry_widget = Entry(frame_widget, font=("Arial", 14))
    entry_widget.bind("<Return>", lambda _: send_message(client_socket, username, text_widget, entry_widget))
    entry_widget.pack(side=LEFT, fill=X, expand=1)

    # Create a button for sending messages
    button_widget = Button(window, text="Send", command=lambda: send_message(client_socket, username, text_widget, entry_widget))
    button_widget.pack(side=RIGHT, padx=5)

    # Create a button for listing all users
    users_widget = Button(window, text="List Users", command=lambda: list_users_request(client_socket))
    users_widget.pack(padx=5, pady=5)

    # Create a button for exiting the chat
    exit_widget = Button(window, text="Exit", command=lambda: exit_request(client_socket, username, window))
    exit_widget.pack(padx=5, pady=5)

    # Start a thread to receive messages from the server
    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()

    # Start the Tkinter main loop
    window.mainloop()

    # Close the client socket when done
    client_socket.close()

if __name__ == '__main__':
    client_program()