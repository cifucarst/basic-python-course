Vamos a crear un **sniffer básico con `threading`** que pueda escuchar en varias interfaces o simular múltiples "clientes" que capturan tráfico al mismo tiempo. Este ejemplo es educativo y muy básico, pero ideal para que entiendas cómo combinar `socket` + `threading` 🧠⚙️.

---

## 🛠️ ¿Qué vamos a hacer?

1. Crear un sniffer que escuche paquetes de red.
2. Usar múltiples hilos para simular varios "sniffers" al mismo tiempo.
3. Mostrar la dirección IP de origen y destino.

> Nota: En Linux necesitarás permisos de superusuario (`sudo`) para usar sockets sin procesar.

---

## 🔒 Sniffer con `threading` — Modo Básico

```python
import socket
import threading

# Crear una función para capturar paquetes
def sniffer(nombre_hilo):
    # Crear un socket sin procesar
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    # En Linux, usar 'eth0' o 'lo'; en Windows puede ser '192.168.x.x'
    sniffer.bind(("0.0.0.0", 0))  # Escucha en todas las interfaces

    # Incluye cabeceras IP
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print(f"[{nombre_hilo}] Sniffer activo...")

    while True:
        paquete, addr = sniffer.recvfrom(65565)
        ip_origen = ".".join(map(str, paquete[12:16]))
        ip_destino = ".".join(map(str, paquete[16:20]))
        print(f"[{nombre_hilo}] {ip_origen} -> {ip_destino}")

# Crear varios hilos de sniffers
for i in range(3):  # Simula 3 sniffers
    hilo = threading.Thread(target=sniffer, args=(f"Sniffer-{i+1}",))
    hilo.daemon = True  # Para que se cierre con el programa
    hilo.start()

# Mantener el programa activo
while True:
    pass
```

---

### 🧪 ¿Qué hace este sniffer?
- Usa sockets sin procesar (`socket.SOCK_RAW`) para capturar paquetes.
- Extrae las IPs del paquete.
- Crea varios hilos que hacen esta tarea en paralelo.
- Imagina que es un sniffer multiproceso, como haría un IDS (sistema de detección de intrusos).

---

## 🧠 Notas importantes

- **Linux**: Este código puede funcionar directamente con `sudo python3 sniffer.py`.
- **Windows**: Necesitas usar WinPcap o librerías como `scapy` o `pyshark`.
- **Seguridad**: Este sniffer no decodifica protocolos. Si quieres leer contenido HTTP, DNS, etc., necesitarás librerías más avanzadas.

---

## ✅ ¿Quieres el próximo paso?

Puedo ayudarte a:

1. **Usar `scapy`** para capturar y analizar paquetes más fácilmente.
2. **Detectar tráfico sospechoso** como escaneos o paquetes anómalos.
3. **Guardar el tráfico en logs o archivos .pcap**.
4. **Crear una interfaz con Flask para mostrar resultados en la web**.

¿Te gustaría avanzar con alguno de esos? O si quieres adaptar este sniffer a algo específico, dime y lo programamos paso a paso 🔍💻