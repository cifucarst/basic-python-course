import socket
import time
from collections import defaultdict

# Configuración
MAX_ATTEMPTS = 3
BLOCK_DURATION = 60  # En segundos
failed_attempts = defaultdict(int)  # Almacena intentos fallidos por IP
blocked_ips = {}  # Almacena IPs bloqueadas y tiempo de desbloqueo

def is_ip_blocked(ip):
    if ip in blocked_ips:
        if time.time() > blocked_ips[ip]:
            del blocked_ips[ip]  # Eliminar IP después del tiempo de bloqueo
            return False
        return True
    return False

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print("Servidor escuchando en el puerto 9999...")

    while True:
        client_socket, address = server_socket.accept()
        ip = address[0]
        
        if is_ip_blocked(ip):
            print(f"IP bloqueada: {ip}")
            client_socket.send(b'Acceso denegado. Su IP está bloqueada.\n'.encode('utf-8'))
            client_socket.close()
            continue

        client_socket.send(b'Introduce la contraseña: '.encode('utf-8'))
        password = client_socket.recv(1024).decode()

        if password == "secreto123":
            client_socket.send(b'Acceso concedido.\n'.decode('utf-8'))
            failed_attempts[ip] = 0  # Restablecer intentos fallidos
        else:
            client_socket.send(b'Acceso denegado.\n'.decode('utf-8'))
            failed_attempts[ip] += 1
            if failed_attempts[ip] >= MAX_ATTEMPTS:
                blocked_ips[ip] = time.time() + BLOCK_DURATION
                print(f"IP bloqueada temporalmente: {ip}")
        client_socket.close()

start_server()