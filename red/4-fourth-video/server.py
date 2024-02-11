#!/usr/bin/env python3

import socket

def start_chat_server():
    host = 'localhost'
    port = 1234

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set socket option to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # TIME_WAIT

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"\n[+] Server ready to accept a connection...")
    
    # Accept a connection
    connection, client_addr = server_socket.accept()
    print(f"\n[+] Client {client_addr} connected")

    while True:
        # Receive a message from the client
        client_message = connection.recv(1024).strip().decode()
        print(f"\n[+] Message from the client: {client_message}")

        # Check if the client wants to end the communication
        if client_message == 'bye':
            break

        # Input a message to send to the client
        server_message = input(f"\n[+] Message to send to the client: ")
        
        # Send the message to the client
        connection.send(server_message.encode())

    # Close the connection
    connection.close()

start_chat_server()