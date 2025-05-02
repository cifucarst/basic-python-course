# 🧪 Ejercicio 3 - Servidor TCP básico
# Escribe un servidor que escuche en el puerto 9999 y muestre cualquier mensaje que reciba de un cliente.

# Pistas:
    # Usa bind(), listen() y accept()
    # Usa un bucle para seguir recibiendo conexiones

import socket

def start_server():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host,port))
        print(f"[+] Servidor escuchando en {host}:{port}")
        sock.listen(1)
        conn, addr = sock.accept()

        with conn:
            print(f"[+] Cliente connectado: {addr}")
            while True:
                data = conn.recv(1024)
                print(f"[+] Mensaje: {data.decode()}")
                
if __name__ == '__main__':
    start_server()