#!/usr/bin/env python3

import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def send_message(client_socket, username, text_widget, entry_widget):
    """
    Sends a message to the server and updates the chat window.
    
    Args:
        client_socket: The socket connected to the server.
        username: The username of the client.
        text_widget: The ScrolledText widget to display chat messages.
        entry_widget: The Entry widget to input chat messages.
    """
    # Get the message from the entry widget
    message = entry_widget.get()
    # Send the message to the server with the username
    client_socket.sendall(f"{username} > {message}".encode())

    # Clear the entry widget after sending the message
    entry_widget.delete(0, END)
    # Enable the text widget to update the chat display
    text_widget.configure(state="normal")
    # Insert the message into the text widget
    text_widget.insert(END, f"{username} > {message}\n")
    # Disable the text widget to prevent user from editing chat history
    text_widget.configure(state="disabled")

def receive_message(client_socket, text_widget):
    """
    Receives messages from the server and updates the chat window.
    
    Args:
        client_socket: The socket connected to the server.
        text_widget: The ScrolledText widget to display chat messages.
    """
    while True:
        try:
            # Receive a message from the server
            message = client_socket.recv(1024).decode()

            # If no message is received, break the loop
            if not message:
                break

            # Enable the text widget to update the chat display
            text_widget.configure(state="normal")
            # Insert the received message into the text widget
            text_widget.insert(END, message)
            # Disable the text widget to prevent user from editing chat history
            text_widget.configure(state="disabled")

        except:
            # If an exception occurs (e.g., server disconnects), break the loop
            break

def client_program():
    """
    Connects to the chat server and sets up the GUI for chat.
    """
    host = 'localhost'  # The server's hostname or IP address
    port = 12345  # The port used by the server

    # Create a socket object for IPv4 and TCP/IP communication
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server's address and port
    client_socket.connect((host, port))

    # Prompt the user to input their username
    username = input(f"\n[+] Enter your username: ")
    # Send the username to the server
    client_socket.sendall(username.encode())

    # Start Tkinter GUI
    window = Tk()
    window.title("Chat")

    # Create a ScrolledText widget to display chat messages
    text_widget = ScrolledText(window, state="disabled")
    text_widget.pack(padx=5, pady=5)

    # Create a frame to hold the entry and button widgets
    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=5, fill=BOTH, expand=1)

    # Create an Entry widget to input chat messages
    entry_widget = Entry(frame_widget)
    # Bind the Enter key to send the message
    entry_widget.bind("<Return>", lambda _: send_message(client_socket, username, text_widget, entry_widget))
    entry_widget.pack(side=LEFT, fill=BOTH, expand=1)

    # Create a Button widget to send the message
    button_widget = Button(frame_widget, text="Send", command=lambda: send_message(client_socket, username, text_widget, entry_widget))
    button_widget.pack(side=RIGHT, padx=5)

    # Create a new thread to handle receiving messages from the server
    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    # Set the thread as a daemon thread so it exits when the main program exits
    thread.daemon = True
    # Start the message receiving thread
    thread.start()

    # Run the Tkinter main loop
    window.mainloop()

    # Close the client socket when done
    client_socket.close()

if __name__ == '__main__':
    # Run the client program when the script is executed
    client_program()