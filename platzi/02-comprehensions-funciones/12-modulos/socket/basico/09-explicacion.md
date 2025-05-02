Vamos a mejorar tu escáner multihilo para que **muestre qué servicio suele estar asociado** a cada puerto abierto. Esto le da un nivel más profesional, como lo hace `nmap`.

---

## 🔧 Parte nueva: Mostrar el servicio de cada puerto

Usaremos un diccionario llamado `common_ports` con los servicios conocidos.

---

### ✅ Código mejorado del escáner: `port_scanner.py`

```python
import socket
import threading

target_ip = '192.168.0.108'
start_port = 1
end_port = 1024
print_lock = threading.Lock()

# Diccionario con puertos comunes y sus servicios
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
            with print_lock:
                print(f"[+] Puerto {port} ABIERTO ({service})")
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

### 🧪 ¿Qué puedes ver?

```bash
[+] Puerto 22 ABIERTO (SSH)
[+] Puerto 80 ABIERTO (HTTP)
[+] Puerto 12345 ABIERTO (Tu servidor de chat 😉)
```

Ya se ve más como una herramienta real de pentesting.  
¿Quieres más precisión? También podrías usar `socket.getservbyport(port)` para obtener el nombre del servicio desde el sistema, aunque a veces da error si no está en `/etc/services`.

---

¿Listo para el **chat multicliente** ahora? ¿O quieres que este escáner también intente detectar el banner del servicio (como hacen algunos escáneres avanzados)?