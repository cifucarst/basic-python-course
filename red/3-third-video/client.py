#!/usr/bin/env python3

import socket

def start_client():
    host = 'localhost'
    port = 1234

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))

        # Continuously send and receive messages until 'bye' is sent
        while True:
            # Input a message from the user
            message = input("\n[+] Enter your message: ")
            
            # Send the message to the server
            s.sendall(message.encode())

            # Check if the message is 'bye' to end the communication
            if message == 'bye':
                break
            
            # Receive a response from the server
            data = s.recv(1024)
            print(f"\n[+] Server response message: {data.decode()}")

start_client()