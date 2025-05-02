💥 Aquí es donde tu chat empieza a parecerse más a una herramienta profesional de comunicación en red 🔌

---

## 🧠 Objetivo: Chat multicliente con `threading`

Queremos que:
1. Un **servidor** escuche conexiones de múltiples clientes.
2. Cada **cliente** que se conecte pueda chatear sin bloquear a los demás.
3. Cuando un cliente envía un mensaje, **todos los demás lo reciben** (tipo sala de chat).

---

### 📁 Estructura básica

- `server.py` → Servidor que maneja múltiples clientes.
- `client.py` → Cada cliente que se conecta al servidor.

---

## 🖥️ `server.py` — Servidor multicliente

```python
import socket
import threading

host = '0.0.0.0'  # Escuchar en todas las interfaces
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

clients = []  # Lista de clientes conectados

print(f"\n[+] Servidor escuchando en {host}:{port}...")

# Función para enviar el mensaje a todos los clientes
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# Función que maneja la conexión con un cliente
def handle_client(client_socket, addr):
    print(f"[+] Cliente {addr} conectado.")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"[{addr}] {message.decode().strip()}")
            broadcast(message, client_socket)
        except:
            break

    print(f"[-] Cliente {addr} desconectado.")
    client_socket.close()
    clients.remove(client_socket)

# Aceptar nuevos clientes
def accept_connections():
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

accept_connections()
```

---

## 💻 `client.py` — Cliente del chat

```python
import socket
import threading

host = '192.168.0.108'  # IP del servidor
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Escuchar mensajes del servidor
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\n[+] Mensaje recibido:", message)
        except:
            print("[-] Conexión cerrada.")
            client.close()
            break

# Enviar mensajes al servidor
def send_messages():
    while True:
        message = input()
        client.send(message.encode())

# Hilos para enviar y recibir al mismo tiempo
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
```

---

## ✅ ¿Cómo probarlo?

1. Ejecuta `server.py` en una máquina (o la tuya).
2. Ejecuta varios `client.py` desde otras terminales (o desde otros PCs en la red).
3. Lo que escribe un cliente, lo ven todos los demás.

---

¿Quieres que el servidor también **muestre nombres de usuario**, o guardar todo el chat en un archivo tipo log (`chatlog.txt`)?  
¿O seguimos subiendo el nivel con alguna mejora tipo comandos especiales (`/exit`, `/list`)?