# 🧪 Ejercicio 2 - Escáner de puerto básico
# Crea un script que reciba una IP y escanee si el puerto 80 está abierto.

# Pistas:
    # Usa socket.connect_ex()
    # Usa settimeout() para evitar que se congele

import socket


def port_scanner(ip: str, port: int):
    """
    Se conecta a una ip y puerto TCP y muestra si el puerto esta abierto o cerrado.

    Args:
        ip (str): La ip de la maquina a escanear.
        puerto (int): El número de puerto al que conectarse.
    """
    try:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.5)
        result = client_socket.connect_ex((ip, port))

        if result == 0:
            print(f"\n[+] Puerto {port} abierto")
        else: 
            print(f"\n[!] puerto {port} cerrado")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        # Cerrar la conexión
        if 'cliente_socket' in locals():
            client_socket.close()
            print("Conexión cerrada.")


if __name__ == '__main__':
    ip: str = '127.0.0.1'
    port = 8080
    port_scanner(ip, port)