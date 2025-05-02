import socket
import threading


def recibir_mensajes(cliente_socket):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode()
            if mensaje:
                print(f"\n[+] Servidor dice: {mensaje}")
                if mensaje.lower() == "bye":
                    break
            else:
                print("\n[+] Conexión con el servidor cerrada.")
                break
        except ConnectionResetError:
            print("\n[+] ¡El servidor cerró la conexión!")
            break
    cliente_socket.close()
    import sys
    sys.exit()


def enviar_mensajes(cliente_socket):
    while True:
        try:
            mensaje = input("[+] Escribe un mensaje para el servidor: ")
            cliente_socket.send(mensaje.encode())
            if mensaje.lower() == "bye":
                break
        except BrokenPipeError:
            print("\n[+] ¡El servidor cerró la conexión inesperadamente!")
            break


def iniciar_cliente():
    host = '192.168.0.108'
    port = 12345

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente_socket.connect((host, port))
        print(f"\n[+] Conectado al servidor en {host}:{port}")
    except socket.error as e:
        print(f"[!] Error al conectar al servidor: {e}")
        return

    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(cliente_socket,))

    hilo_recibir.start()
    hilo_enviar.start()

    hilo_recibir.join()
    hilo_enviar.join()
    print("\n[+] Conexión cerrada.")
    cliente_socket.close()


if __name__ == "__main__":
    iniciar_cliente()