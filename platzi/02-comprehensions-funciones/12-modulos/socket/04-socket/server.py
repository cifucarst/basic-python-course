import socket

PASSWORD = "secreto123"

def start_auth_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    print("Servidor de autenticación escuchando...")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Conexión desde {address}")
        # Usamos encode() para manejar caracteres no ASCII
        client_socket.send('Introduce la contraseña: '.encode('utf-8'))
        password = client_socket.recv(1024).decode('utf-8')
        
        if password == PASSWORD:
            client_socket.send('Acceso concedido.\n'.encode('utf-8'))
        else:
            client_socket.send('Acceso denegado.\n'.encode('utf-8'))
        client_socket.close()

start_auth_server()