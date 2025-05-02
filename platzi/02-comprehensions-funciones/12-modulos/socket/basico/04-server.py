import socket
import threading

def recibir_mensajes(conexion):
    while True:
        try:
            mensaje = conexion.recv(1024).decode()
            if mensaje:
                print(f"\n[+] Cliente dice: {mensaje}")
                if mensaje.lower() == "bye":
                    break
            else:
                break
        except ConnectionResetError:
            print("\n[+] ¡Conexión con el cliente perdida!")
            break
    conexion.close()


def enviar_mensajes(conexion):
    while True:
        try:
            mensaje = input("[+] Escribe un mensaje para el cliente: ")
            conexion.send(mensaje.encode())
            if mensaje.lower() == "bye":
                break
        except BrokenPipeError:
            print("\n[+] ¡El cliente cerró la conexión inesperadamente!")
            break


def manejar_cliente(conexion, direccion):
    print(f"\n[+] Conexión aceptada de {direccion}")

    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(conexion,))
    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(conexion,))

    hilo_recibir.start()
    hilo_enviar.start()

    hilo_recibir.join()
    hilo_enviar.join()
    print(f"\n[+] Conexión con {direccion} finalizada.")
    conexion.close()


def iniciar_servidor():
    host = '192.168.0.108'
    port = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        servidor.bind((host, port))
    except socket.error as e:
        print(f"[!] Error al enlazar el socket: {e}")
        return

    servidor.listen(1)
    print(f"\n[+] Servidor listo para conexiones en {host}:{port}...")

    while True:
        try:
            conexion, direccion_cliente = servidor.accept()
            hilo_cliente = threading.Thread(target=manejar_cliente, args=(conexion, direccion_cliente))
            hilo_cliente.start()
        except KeyboardInterrupt:
            print("\n[+] Cerrando el servidor...")
            break
    servidor.close()

if __name__ == "__main__":
    iniciar_servidor()