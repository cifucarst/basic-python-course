¡Perfecto! 🚀 Vamos a crear ahora un **cliente sencillo** en Python que se conecte al servidor que programaste.

Aquí tienes el **código del cliente** explicado paso a paso también:

```python
import socket

def start_client():
    host = 'localhost'
    port = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print(f"[+] Conectado al servidor {host}:{port}")

        while True:
            message = input("Escribe un mensaje (o 'salir' para terminar): ")
            if message.lower() == 'salir':
                print("[!] Cerrando conexión")
                break
            sock.sendall(message.encode())

if __name__ == '__main__':
    start_client()
```

---

## Ahora te explico qué hace cada parte:

### `import socket`
- Importamos el módulo `socket`, igual que en el servidor.

---

### `def start_client():`
- Definimos una función para encapsular el cliente.

---

### `host = 'localhost'`
### `port = 9999`
- Le decimos que el cliente se va a conectar a `localhost` y al puerto `9999`, que es donde está escuchando tu servidor.

---

### `with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:`
- Creamos un socket **TCP/IP** (IPv4 y conexión orientada a flujo).

---

### `sock.connect((host, port))`
- Nos **conectamos** al servidor que está en esa dirección IP y puerto.

---

### `print(f"[+] Conectado al servidor {host}:{port}")`
- Confirmamos que la conexión fue exitosa.

---

### `while True:`
- Un bucle infinito donde pediremos al usuario que escriba mensajes para enviar al servidor.

---

### `message = input("Escribe un mensaje (o 'salir' para terminar): ")`
- Solicitamos un mensaje al usuario.

---

### `if message.lower() == 'salir':`
- Si el usuario escribe "salir" (en minúscula, usando `.lower()`), entonces terminamos la conexión.

---

### `sock.sendall(message.encode())`
- Si no escribió "salir", enviamos el mensaje al servidor.
- `.sendall()` envía todos los bytes del mensaje codificado.
- `.encode()` convierte el string en bytes, porque la red trabaja con bytes.

---

### `if __name__ == '__main__':`
### `start_client()`
- Ejecutamos el cliente si el script es ejecutado directamente.

---

# ¿Cómo probarlo?

1. **Primero** corre el **servidor**:  
   Ejecuta tu archivo del servidor (`python servidor.py`) y espera a que diga que está escuchando.

2. **Segundo** corre el **cliente**:  
   Ejecuta este cliente (`python cliente.py`) y verás que se conecta.

3. **Tercero** envía mensajes:  
   Escribe mensajes en la terminal del cliente, y verás que **aparecen en la terminal del servidor**.

4. **Para salir**:  
   Escribe `salir` en el cliente y la conexión se cerrará.

---

¿Quieres que también te muestre cómo hacer que el servidor acepte **múltiples clientes al mismo tiempo** usando `threads`? 🔥🚀  
¡Eso sería un siguiente paso genial!