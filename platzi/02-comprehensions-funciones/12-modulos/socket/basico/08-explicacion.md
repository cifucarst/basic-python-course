Estás apuntando alto, eso me encanta 🔥  
Vamos a ir por partes, como dijiste antes. Empezamos con el **escáner de puertos multihilo**, y luego hacemos el **servidor multicliente** para el chat.

---

## 🔍 Parte 1: Escáner de puertos multihilo en Python

Con esto vas a poder escanear **muchos puertos rápidamente** porque cada puerto lo revisa un hilo separado.

---

### ✅ Código completo: `port_scanner.py`

```python
import socket
import threading

# Dirección IP que quieres escanear
target_ip = '192.168.0.108'

# Rango de puertos que quieres escanear
start_port = 1
end_port = 1024

# Mutex para imprimir sin que los hilos se crucen
print_lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Tiempo de espera por puerto
        result = sock.connect_ex((target_ip, port))  # 0 = abierto
        if result == 0:
            with print_lock:
                print(f"[+] Puerto {port} está ABIERTO")
        sock.close()
    except:
        pass

# Crear un hilo por puerto
def main():
    print(f"\n[+] Escaneando puertos en {target_ip}...\n")
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    # Esperar que todos los hilos terminen
    for t in threads:
        t.join()

    print("\n[+] Escaneo finalizado.")

if __name__ == "__main__":
    main()
```

---

### 🧠 Explicación rápida

| Parte | ¿Qué hace? |
|-------|------------|
| `connect_ex` | Intenta conectarse al puerto. Si da 0, el puerto está abierto. |
| `threading.Thread` | Crea un hilo para cada puerto. |
| `print_lock` | Asegura que los mensajes no se mezclen en la consola. |
| `.join()` | Espera a que todos los hilos terminen antes de mostrar "Escaneo finalizado". |

---

### 🧪 ¿Cómo probarlo?

1. Ejecuta algún servicio en tu máquina, como tu chat en el puerto 12345.
2. Ejecuta este escáner apuntando a esa IP.
3. Deberías ver algo como:
   ```
   [+] Puerto 22 está ABIERTO
   [+] Puerto 80 está ABIERTO
   [+] Puerto 12345 está ABIERTO
   ```

---

¿Quieres que este escáner también **muestre qué servicio hay en cada puerto** (como SSH, HTTP, etc.)?  
¿O pasamos de una al servidor multicliente ahora?