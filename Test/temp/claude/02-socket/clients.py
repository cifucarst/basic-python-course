import socket

def start_client():
    SERVER_HOST = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, port))
        print(f"Connected to server at {SERVER_HOST}:{port}")

        try:
            while True:
                msg = input("You: ")
                if msg.lower() == 'exit':
                    break
                s.sendall(msg.encode())
                data = s.recv(1024)
                print(f"Server: {data.decode()}")
        finally:
            s.close()

start_client()