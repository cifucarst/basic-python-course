import socket

def port_scanner(ip: str, port: int):
    """
    Se conecta a una IP y puerto TCP y muestra si el puerto está abierto o cerrado.

    Args:
        ip (str): La IP de la máquina a escanear.
        port (int): El número de puerto al que conectarse.
    """
    client_socket = None
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.5)
        result = client_socket.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Puerto {port} abierto")
        else:
            print(f"[!] Puerto {port} cerrado")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        if client_socket:
            client_socket.close()
            print("Conexión cerrada.")

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 8080
    port_scanner(ip, port)