#!/usr/bin/env python3

import socket

def start_client():
    host = 'localhost'
    port = 1234

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        
        # Send a message to the server
        s.sendall(b"Hello, server!")
        
        # Receive data from the server
        data = s.recv(1094)

    # Print the message received from the server
    print(f"\n[+] Message received from the server: {data.decode()}")

start_client()