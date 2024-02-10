#!/usr/bin/env python3

import socket

def start_server():
    host = 'localhost'
    port = 1234

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the host and port
        s.bind((host, port))
        print(f"\n[+] Server listening on {host}:{port}")
        
        # Listen for incoming connections
        s.listen(1)
        
        # Accept a connection
        conn, addr = s.accept()

        # Handle the connection
        with conn:
            print(f"\n[+] A new client has connected: {addr}")
            
            # Receive and echo data back to the client
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

start_server()