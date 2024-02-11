#!/usr/bin/env python3

import socket
import threading
import pdb  # Debugging

class ClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        # Print a message when a new client is connected
        print(f"\n[+] New client connected: {client_addr}")

    def run(self):
        message = ''
        while True:
            # Receive data from the client
            data = self.client_sock.recv(1024)
            message = data.decode()

            # Check if the client sent 'bye' to disconnect
            if message.strip() == 'bye':
                break
            
            # Print the message sent by the client
            print(f"\n[+] Message sent by the client: {message.strip()}")

            # Send the received data back to the client
            self.client_sock.send(data)

        # Print a message when the client is disconnected
        print(f"\n[+] Client {self.client_addr} disconnected")

        # Close the client socket
        self.client_sock.close()

HOST = 'localhost'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Set socket option to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # TIME_WAIT

    # Bind the server socket to the specified host and port
    server_socket.bind((HOST, PORT))

    # Print a message indicating the server is waiting for incoming connections
    print(f"\n[+] Waiting for incoming connections...")

    while True:
        # Listen for incoming connections
        server_socket.listen()

        # Accept a new connection
        client_sock, client_addr = server_socket.accept()

        # Create a new thread to handle the client
        new_thread = ClientThread(client_sock, client_addr)
        
        # Start the thread, which will execute the run method
        new_thread.start()  # run()