#!/usr/bin/env python3

import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the server address
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

try:
    # Define a message to be sent to the server
    message = b"This is a test message I am sending to the server"

    # Send the message to the server
    client_socket.sendall(message)

    # Receive data from the server
    data = client_socket.recv(1024)

    # Print the response received from the server
    print(f"\n[+] The server has responded with this message: {data.decode()}")

finally:
    # Close the client socket
    client_socket.close()