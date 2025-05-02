 Ahora vamos a mejorar tu escáner para que además de decir **"el puerto está abierto"**, también intente **conectarse y leer un banner** del servicio (si este lo muestra). Esto ya es comportamiento de escáneres como `nmap -sV` o herramientas más especializadas.

---

## 📜 ¿Qué es un *banner*?

Un **banner** es un mensaje que algunos servicios envían al conectar. Por ejemplo:
- Un servidor FTP puede responder con:  
  `"220 ProFTPD 1.3.6 Server ready"`
- Un servidor HTTP puede darte algo como:  
  `"HTTP/1.1 400 Bad Request"`

Eso nos da pistas de:
- Qué servicio es.
- Qué versión.
- Qué software.

---

## 🔐 Importante

No todos los servicios envían banners. Algunos solo lo hacen **si les escribes algo primero**, y otros simplemente no responden.

---

## ✅ Código del escáner con detección de banners

```python
import socket
import threading

target_ip = '192.168.0.108'
start_port = 1
end_port = 1024
print_lock = threading.Lock()

common_ports = {
    20: "FTP (data)",
    21: "FTP (control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP (TLS)",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-alt",
    12345: "Tu servidor de chat 😉"
}

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = common_ports.get(port, "Servicio desconocido")

            # Intentamos leer el banner
            try:
                banner = sock.recv(1024).decode().strip()
                if not banner:
                    banner = "(No banner recibido)"
            except:
                banner = "(Error al recibir banner)"

            with print_lock:
                print(f"[+] Puerto {port} ABIERTO ({service})")
                print(f"    └─ Banner: {banner}")

        sock.close()
    except:
        pass

def main():
    print(f"\n[+] Escaneando puertos en {target_ip}...\n")
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Escaneo finalizado.")

if __name__ == "__main__":
    main()
```

---

### 🧪 Ejemplo de salida:

```
[+] Puerto 21 ABIERTO (FTP (control))
    └─ Banner: 220 ProFTPD 1.3.5e Server ready

[+] Puerto 80 ABIERTO (HTTP)
    └─ Banner: HTTP/1.1 400 Bad Request

[+] Puerto 12345 ABIERTO (Tu servidor de chat 😉)
    └─ Banner: (No banner recibido)
```

---

¿Listo para ir ahora al **chat multicliente**?  
¿O quieres que este escáner guarde la salida en un archivo tipo `.txt` para tener un "reporte"?