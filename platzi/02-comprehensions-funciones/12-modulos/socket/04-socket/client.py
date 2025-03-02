import socket

def brute_force():
    passwords = ["12345", "admin", "secreto123", "root"]
    for password in passwords:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(('127.0.0.1', 8888))
            print(client_socket.recv(1024).decode())
            client_socket.send(password.encode())
            response = client_socket.recv(1024).decode()
            print(f"Intento con '{password}': {response}")
            if "concedido" in response:
                print("¡Contraseña encontrada!")
                break
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

brute_force()