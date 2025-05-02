# 🧪 Ejercicio 1 - Cliente TCP simple
# Crea un programa que se conecte a un servidor web (por ejemplo, example.com) por el puerto 80 y muestre la IP a la que se conecta.

# Pistas:

# Usa socket.gethostbyname()
# Usa socket.socket() y connect()

import socket


def cliente_tcp_simple(servidor, puerto):
    """
    Se conecta a un servidor TCP y muestra la IP a la que se conecta.

    Args:
        servidor (str): El nombre de dominio o la dirección IP del servidor.
        puerto (int): El número de puerto al que conectarse.
    """
    try:
        # Obtener la dirección IP del servidor a partir de su nombre de dominio
        ip_servidor = socket.gethostbyname(servidor)
        print(f"Intentando conectar a: {servidor} ({ip_servidor}) en el puerto {puerto}")

        # Crear un socket TCP
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectar al servidor
        cliente_socket.connect((ip_servidor, puerto))
        print("¡Conexión exitosa!")

        

    except socket.gaierror:
        print(f"Error: No se pudo resolver la dirección del servidor: {servidor}")
    except ConnectionRefusedError:
        print(f"Error: Conexión rechazada por el servidor en {servidor}:{puerto}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        # Cerrar la conexión
        if 'cliente_socket' in locals():
            cliente_socket.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    servidor_objetivo = 'platzi.com'
    # servidor_objetivo = "example.com"
    puerto_objetivo = 8080
    cliente_tcp_simple(servidor_objetivo, puerto_objetivo)