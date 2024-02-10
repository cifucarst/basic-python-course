#!/usr/bin/env python3

import socket

def start_udp_server():
    host = 'localhost'
    port = 1234

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Bind the socket to the host and port
        s.bind((host, port))
        print(f"\n[+] UDP Server listening on {host}:{port}")

        # Receive and process incoming data
        while True:
            data, addr = s.recvfrom(1024)
            print(f"\n[+] Message sent by the user: {data.decode()}")
            print(f"\n[+] Information of the user sending the information: {addr}")

start_udp_server()