# 🧪 Ejercicio 4 - Cliente-Servidor de eco
# Haz un programa donde:
    # El servidor recibe un mensaje y lo devuelve tal cual al cliente.
    # El cliente manda un mensaje por consola y muestra la respuesta del servidor.

import socket

def start_server():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        print(f"[+] Servidor escuchando en {host}:{port}")
        sock.listen(5)
        conn, addr = sock.accept()

        with conn: 
            print(f"[+] Nuevo servidor connectado: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"[-] Cliente desconectado")
                    break
                print(f"[+] Mensaje del cliente: {data.decode()}")
                conn.sendall(data)


if __name__ == '__main__':
    start_server()