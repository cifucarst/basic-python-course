import socket

def start_server():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(5)
        print(f"[+] Servidor escuchando en {host}:{port}")

        conn, addr = sock.accept()
        with conn:
            print(f"[+] Cliente conectado: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[!] Cliente desconectado")
                    break
                print(f"[+] Mensaje: {data.decode()}")

if __name__ == '__main__':
    start_server()