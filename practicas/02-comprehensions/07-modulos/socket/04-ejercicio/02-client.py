import socket

def start_client():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        print(f"[+] Connectado al servidor en {host}:{port}")
        sock.sendall(b"hello server")
        data = sock.recv(1024)

    print(f"[+] Respuesta del servidor: {data.decode()}")


if __name__ == '__main__':
    start_client()