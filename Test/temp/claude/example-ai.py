import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(f"\nServer: {message}")
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    try:
        while True:
            msg = input("You: ")
            if msg.lower() == 'exit':
                break
            client_socket.send(msg.encode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()