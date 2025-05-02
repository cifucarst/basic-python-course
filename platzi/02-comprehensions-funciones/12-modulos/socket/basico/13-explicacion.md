¡Eso es, Andrés! 🔥 Ahora tu servidor no solo va a manejar chats normales, sino que **también será capaz de administrar** el chat con **comandos especiales** como un verdadero administrador 👨‍💻👑.

---

## ✅ Objetivos de esta mejora:

- El **servidor** podrá escribir **comandos administrativos** directamente en su terminal.
- Comandos que vamos a agregar:
  - `/list` → Mostrar todos los usuarios conectados.
  - `/kick usuario` → Expulsar a un usuario del chat.
  - `/shutdown` → Cerrar todo el servidor (opcional, si quieres).

---

## 📁 Vamos a mejorar el `server.py`

Antes, **el servidor solo aceptaba conexiones** y escuchaba a los clientes.  
Ahora, **el servidor también escuchará tus propios comandos** mientras está funcionando.

### 💡 Nueva idea:
Tendremos un **hilo para aceptar conexiones** y otro **hilo para leer los comandos administrativos**.

---

### 🧠 `server.py` mejorado con comandos admin

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

def save_to_log(message):
    with open("chatlog.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

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
        client_socket.send("Escribe tu nombre de usuario: ".encode())
        username = client_socket.recv(1024).decode().strip()
        client_usernames[client_socket] = username
        clients.append(client_socket)

        welcome_msg = f"[+] {username} se ha unido al chat."
        print(welcome_msg)
        broadcast(welcome_msg)
        save_to_log(welcome_msg)

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
        if client_socket in clients:
            left_msg = f"[-] {client_usernames[client_socket]} ha salido del chat."
            print(left_msg)
            broadcast(left_msg)
            save_to_log(left_msg)
            clients.remove(client_socket)
            del client_usernames[client_socket]
            client_socket.close()

# Hilo para aceptar nuevas conexiones
def accept_connections():
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

# Hilo para comandos administrativos
def admin_commands():
    while True:
        command = input()

        if command == "/list":
            print("\nUsuarios conectados:")
            for username in client_usernames.values():
                print(f" - {username}")

        elif command.startswith("/kick"):
            try:
                _, username_to_kick = command.split()
                socket_to_kick = None

                for client_socket, username in client_usernames.items():
                    if username == username_to_kick:
                        socket_to_kick = client_socket
                        break

                if socket_to_kick:
                    kick_msg = "Has sido expulsado del chat por el administrador."
                    socket_to_kick.send(kick_msg.encode())
                    socket_to_kick.close()
                    clients.remove(socket_to_kick)
                    del client_usernames[socket_to_kick]
                    broadcast(f"[-] {username_to_kick} fue expulsado del chat.")
                    save_to_log(f"[-] {username_to_kick} fue expulsado del chat.")
                    print(f"[+] Usuario {username_to_kick} expulsado.")
                else:
                    print(f"[-] Usuario {username_to_kick} no encontrado.")

            except Exception as e:
                print("[-] Error al usar /kick. Uso correcto: /kick nombre_usuario")

        elif command == "/shutdown":
            print("[+] Apagando el servidor...")
            for client in clients:
                try:
                    client.send("Servidor cerrando...".encode())
                    client.close()
                except:
                    pass
            server.close()
            break

        else:
            print("[-] Comando desconocido.")

# Iniciar los hilos
threading.Thread(target=accept_connections).start()
threading.Thread(target=admin_commands).start()
```

---

## 🔥 Ahora el servidor puede:

| Comando | ¿Qué hace? |
|:---|:---|
| `/list` | Ver todos los usuarios conectados. |
| `/kick nombre_usuario` | Expulsar a alguien del chat. |
| `/shutdown` | Cerrar todo el servidor y desconectar a todos. |

---

## 💬 ¿Qué pasa con `client.py`?
- No necesita cambios en este momento.
- Si el cliente recibe un mensaje tipo "Has sido expulsado" o "Servidor cerrando...", simplemente lo va a mostrar y cerrar conexión si quieres más adelante.

---

## 🧠 ¿Qué entendiste hasta aquí?

¿Quieres que ahora también le pongamos una pequeña mejora para que **el cliente detecte si fue kickeado o si el servidor se apaga** y que cierre bien sin errores? 🚀  
¿O prefieres agregar **comandos para los propios usuarios** tipo `/users` para ver cuántos hay conectados sin ser admin?