import socket

def connect_to_server():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    print(client_socket.recv(1024).decode())
    client_socket.send(b'Gracias, servidor.\n')
    
    client_socket.close()

connect_to_server()