#!/usr/bin/env python3

import socket

def start_chat_client():
    host = 'localhost'
    port  = 1234

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))

    while True:
        # Input a message to send to the server
        client_message = input(f"\n[+] Message to send to the server: ")
        
        # Send the message to the server
        client_socket.send(client_message.encode())

        # Check if the message is 'bye' to end the communication
        if client_message == 'bye':
            break
        
        # Receive a message from the server
        server_message = client_socket.recv(1024).strip().decode()
        print(f"\n[+] Server message: {server_message}")

    # Close the client socket
    client_socket.close()

start_chat_client()