#!/usr/bin/env python3

import socket

def start_udp_client():
    host = 'localhost'
    port = 1234

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Encode the message to bytes
        message = "Hello, test message".encode("utf-8")
        
        # Send the message to the server
        s.sendto(message, (host, port))

start_udp_client()