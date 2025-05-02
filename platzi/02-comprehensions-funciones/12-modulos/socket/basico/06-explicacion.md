 Vamos a convertir tu chat básico en un **chat multihilo**, para que puedas **enviar y recibir mensajes al mismo tiempo** sin que el programa se congele esperando input. Esto es esencial para simular herramientas más realistas en ciberseguridad, como troyanos o shells remotas.

---

## 🎯 ¿Qué vamos a hacer con `threading`?

Vamos a crear **dos hilos**:
- Uno para **recibir mensajes**
- Otro para **enviar mensajes**

Cada uno corre en paralelo, así el usuario puede escribir y leer sin bloquear al otro.

---

## ✅ Versión mejorada del **Servidor** con `threading`

```python
# server.py
import socket
import threading

def recibir_mensajes(connection):
    while True:
        try:
            mensaje = connection.recv(1024).decode()
            if mensaje.lower() == "bye":
                print("\n[+] El cliente ha cerrado la conexión.")
                break
            print(f"\n[Cliente]: {mensaje}")
        except:
            print("\n[!] Error al recibir mensaje.")
            break

def enviar_mensajes(connection):
    while True:
        try:
            mensaje = input("[Tú]: ")
            connection.send(mensaje.encode())
            if mensaje.lower() == "bye":
                break
        except:
            print("\n[!] Error al enviar mensaje.")
            break

def start_chat_server():
    host = '192.168.0.108'
    port = 12345

    start_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    start_server.bind((host, port))
    start_server.listen(1)

    print(f"\n[+] Servidor escuchando en {host}:{port}...")
    connection, client_addr = start_server.accept()
    print(f"[+] Cliente conectado desde: {client_addr}")

    # Iniciar hilos
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(connection,))
    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(connection,))
    hilo_recibir.start()
    hilo_enviar.start()

    hilo_recibir.join()
    hilo_enviar.join()
    connection.close()
    print("\n[+] Conexión cerrada.")

start_chat_server()
```

---

## ✅ Versión mejorada del **Cliente** con `threading`

```python
# client.py
import socket
import threading

def recibir_mensajes(start_client):
    while True:
        try:
            mensaje = start_client.recv(1024).decode()
            if mensaje.lower() == "bye":
                print("\n[+] El servidor ha cerrado la conexión.")
                break
            print(f"\n[Servidor]: {mensaje}")
        except:
            print("\n[!] Error al recibir mensaje.")
            break

def enviar_mensajes(start_client):
    while True:
        try:
            mensaje = input("[Tú]: ")
            start_client.send(mensaje.encode())
            if mensaje.lower() == "bye":
                break
        except:
            print("\n[!] Error al enviar mensaje.")
            break

def start_chat_client():
    host = '192.168.0.108'
    port = 12345

    start_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_client.connect((host, port))

    # Iniciar hilos
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(start_client,))
    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(start_client,))
    hilo_recibir.start()
    hilo_enviar.start()

    hilo_recibir.join()
    hilo_enviar.join()
    start_client.close()
    print("\n[+] Conexión cerrada.")

start_chat_client()
```

---

## 🧪 ¿Cómo probarlo?

1. En una terminal, ejecuta `server.py`.
2. En otro computador de tu red, ejecuta `client.py`.
3. ¡Chatea sin bloqueos! Ahora puedes escribir sin esperar que el otro responda.

---

¿Te gustaría que te explique **cómo funciona exactamente `threading.Thread` y por qué usamos `.join()`**? ¿O prefieres pasar directo al próximo reto como el escáner multihilo?