#!/usr/bin/env python3

import socket
import threading

def client_thread(client_socket, clients, usernames):
    """
    Handles communication with the connected client.
    Receives the username, notifies other clients, and relays messages.
    
    Args:
        client_socket: The socket connected to the client.
        clients: A list of all connected client sockets.
        usernames: A dictionary mapping client sockets to usernames.
    """
    # Receive the username from the client
    username = client_socket.recv(1024).decode()
    # Store the username associated with the client socket
    usernames[client_socket] = username

    print(f"\n[+] User {username} has connected to the chat")

    # Notify all other clients about the new user
    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] User {username} has entered the chat\n\n".encode())

    while True:
        try:
            # Receive a message from the client
            message = client_socket.recv(1024).decode()

            # If no message is received, break the loop
            if not message:
                break

            # Relay the message to all other clients
            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())

        except:
            # If an exception occurs (e.g., client disconnects), break the loop
            break

def server_program():
    """
    Sets up the server to accept incoming client connections.
    """
    host = 'localhost'  # Server will listen on localhost
    port = 12345  # Server will listen on port 12345

    # Create a socket object for IPv4 and TCP/IP communication
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow the socket to reuse the address, useful for quick restarts
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    # Enable the server to accept connections (with a backlog of connections)
    server_socket.listen()

    print(f"\n[+] The server is listening for incoming connections...")

    clients = []  # List to keep track of all connected clients
    usernames = {}  # Dictionary to store usernames of connected clients

    while True:
        # Accept a new client connection
        client_socket, address = server_socket.accept()
        # Add the client socket to the clients list
        clients.append(client_socket)

        print(f"\n[+] A new client has connected: {address}")

        # Create a new thread to handle communication with the connected client
        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        # Set the thread as a daemon thread so it exits when the main program exits
        thread.daemon = True
        # Start the client handling thread
        thread.start()

    # Close the server socket (not reachable here as the while loop runs indefinitely)
    server_socket.close()

if __name__ == '__main__':
    # Run the server program when the script is executed
    server_program()