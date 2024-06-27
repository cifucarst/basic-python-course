#!/usr/bin/env python3

import socket

def client_program():
    """
    Connects to the server and sends the username.
    """
    host = 'localhost'  # The server's hostname or IP address
    port = 1234  # The port used by the server

    # Create a socket object for IPv4 and TCP/IP communication
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server's address and port
    client_socket.connect((host, port))

    # Prompt the user to input their username
    username = input(f"\n[+] Enter your username: ")
    # Send the username to the server
    client_socket.sendall(username.encode())

    # Close the client socket
    client_socket.close()

if __name__ == '__main__':
    # Run the client program when the script is executed
    client_program()
