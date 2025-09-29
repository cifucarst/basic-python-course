import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_address = ("localhost", 1234)
client_socket.connect(client_address)

try:
    message = b"This is a test message"
    client_socket.send(message)
    data = client_socket.recv(1024)

    print(f"\n[+] Message from the server: {data.decode()}")
finally:
    client_socket.close()
