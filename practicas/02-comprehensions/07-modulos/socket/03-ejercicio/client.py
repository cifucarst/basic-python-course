import socket

def start_client():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print(f"[+] Conectado al servidor {host}:{port}")

        while True:
            message = input("Escribe un mensaje (o 'salir' para terminar): ")
            if message.lower() == 'salir':
                print("[!] Cerrando conexión")
                break
            sock.sendall(message.encode())

if __name__ == '__main__':
    start_client()