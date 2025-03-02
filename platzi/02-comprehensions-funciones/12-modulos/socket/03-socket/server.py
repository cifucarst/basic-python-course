import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print("Servidor escuchando en el puerto 9999...")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Conexión aceptada de {address}")
        client_socket.send(b'Hola, bienvenido al servidor.\n')
        data = client_socket.recv(1024)
        print(f"Recibido: {data.decode()}")
        client_socket.close()

start_server()