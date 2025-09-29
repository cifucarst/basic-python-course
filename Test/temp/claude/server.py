import socket

def start_server():
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind
