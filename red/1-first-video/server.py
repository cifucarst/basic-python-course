#!/usr/bin/env python3

import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the server address
server_address = ('localhost', 12345)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections, allowing a maximum of 1 connection in the queue
server_socket.listen(1)

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()

    # Receive data from the client
    data = client_socket.recv(1024)

    # Display the received message from the client
    print(f"\n[+] Message received from the client: {data.decode()}")

    # Display information about the connected client
    print(f"[+] Information of the client who has connected with us: {client_address}")

    # Send a greeting message back to the client
    client_socket.sendall(f"Greetings mate\n".encode())

    # Close the connection with the client
    client_socket.close()