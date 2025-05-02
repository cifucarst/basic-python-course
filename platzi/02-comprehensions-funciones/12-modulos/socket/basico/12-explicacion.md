Vamos a mejorar tu **chat multicliente** con dos cosas:

---

## ✅ Objetivos nuevos:

1. **Agregar nombre de usuario** cuando alguien entra al chat.
2. **Guardar el historial del chat** en un archivo `chatlog.txt`.
3. **Soportar comandos especiales** como `/exit` para salir.

Te voy explicando paso por paso para que entiendas cómo funciona cada cosa.

---

## 📁 Empezamos con el Servidor (`server.py`)

### 💡 Cambios importantes:

- Se pedirá el **nombre de usuario** al conectarse.
- Se usará un diccionario `client_usernames` para guardar qué socket tiene qué usuario.
- Se usará una función `save_to_log()` para guardar todo en `chatlog.txt`.

---

### 🧠 `server.py` con mejoras:

```python
import socket
import threading
from datetime import datetime

host = '0.0.0.0'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

clients = []
client_usernames = {}

print(f"\n[+] Servidor escuchando en {host}:{port}...")

# Guardar mensajes en un archivo
def save_to_log(message):
    with open("chatlog.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

# Enviar mensaje a todos menos al emisor
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket, addr):
    try:
        # Pedir nombre de usuario
        client_socket.send("Escribe tu nombre de usuario: ".encode())
        username = client_socket.recv(1024).decode().strip()
        client_usernames[client_socket] = username
        clients.append(client_socket)

        welcome_msg = f"[+] {username} se ha unido al chat."
        print(welcome_msg)
        broadcast(welcome_msg)
        save_to_log(welcome_msg)

        # Recibir mensajes del cliente
        while True:
            message = client_socket.recv(1024).decode()
            if message == "/exit":
                break

            full_message = f"{username}: {message}"
            print(full_message)
            broadcast(full_message, client_socket)
            save_to_log(full_message)

    except Exception as e:
        print(f"Error con {addr}: {e}")

    finally:
        left_msg = f"[-] {client_usernames[client_socket]} ha salido del chat."
        print(left_msg)
        broadcast(left_msg)
        save_to_log(left_msg)
        clients.remove(client_socket)
        del client_usernames[client_socket]
        client_socket.close()

# Escuchar conexiones entrantes
def accept_connections():
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

accept_connections()
```

---

## 💻 `client.py` mejorado

### 💡 Cambios:

- Al conectarse, el servidor pide el nombre de usuario.
- El cliente puede escribir `/exit` para cerrar.

---

### 🧠 `client.py` actualizado:

```python
import socket
import threading

host = '192.168.0.108'  # Cambia esto según el servidor
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("[-] Conexión cerrada.")
            break

def send_messages():
    while True:
        message = input()
        client.send(message.encode())
        if message == "/exit":
            break
    client.close()

# Recibir mensaje inicial del servidor
first_message = client.recv(1024).decode()
print(first_message)
username = input()
client.send(username.encode())

# Iniciar hilos
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
```

---

## 🧪 ¿Qué puedes hacer ahora?

- Cuando alguien entra, escribe su **nombre de usuario**.
- Todos ven su nombre en los mensajes.
- Al escribir `/exit`, se sale del chat.
- Todo se guarda en un archivo `chatlog.txt`.

---

¿Te gustaría que el servidor tenga comandos administrativos? Por ejemplo:
- `/list` para ver qué usuarios están conectados.
- `/kick usuario` para sacar a alguien del chat.

O si quieres, podemos mejorar el cliente con interfaz básica o más comandos. ¿Qué te gustaría agregarle ahora?