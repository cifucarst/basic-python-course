### 🔥 **Ejemplo avanzado en ciberseguridad: Escaneo de red en paralelo con ARP**
Este script escanea una red completa utilizando solicitudes ARP en paralelo, ayudándonos a identificar dispositivos activos.

#### 📌 **¿Cómo funciona?**
1. Obtiene la dirección IP de la interfaz de red.
2. Calcula el rango de direcciones IP en la subred.
3. Usa `multiprocessing` para enviar solicitudes ARP en paralelo.
4. Muestra las direcciones IP y MAC de los dispositivos detectados.

---

### 🔹 **Código: Escaneo de red con `multiprocessing` y Scapy**
```python
import multiprocessing
import scapy.all as scapy
import ipaddress
import netifaces

def get_local_network():
    """ Obtiene la dirección IP de la interfaz de red y la convierte en un rango de IPs """
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]  # Obtiene la interfaz activa
    ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    
    local_ip = ip_info['addr']  # Dirección IP local
    subnet_mask = ip_info['netmask']  # Máscara de subred
    
    network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict=False)
    return network

def arp_scan(ip):
    """ Envía una solicitud ARP y verifica si hay respuesta """
    arp_request = scapy.ARP(pdst=str(ip))
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    response = scapy.srp(packet, timeout=1, verbose=False)[0]

    for sent, received in response:
        print(f"[+] Dispositivo encontrado: {received.psrc} - {received.hwsrc}")

if __name__ == "__main__":
    network = get_local_network()
    
    print(f"Escaneando red: {network}")
    
    with multiprocessing.Pool(processes=10) as pool:
        pool.map(arp_scan, [ip for ip in network.hosts()])
    
    print("Escaneo finalizado.")
```

---

### 🔹 **Explicación del código**
1. **`get_local_network()`**  
   - Obtiene la dirección IP local y la máscara de subred.
   - Calcula el rango de direcciones IP de la red usando `ipaddress`.

2. **`arp_scan(ip)`**  
   - Crea un paquete ARP para solicitar la dirección MAC de `ip`.
   - Envía el paquete y espera respuestas.
   - Si recibe una respuesta, imprime la IP y la MAC del dispositivo.

3. **`multiprocessing.Pool`**  
   - Lanza 10 procesos simultáneamente para escanear la red más rápido.

---

### 📌 **Salida esperada**
```
Escaneando red: 192.168.1.0/24
[+] Dispositivo encontrado: 192.168.1.1 - AA:BB:CC:DD:EE:FF
[+] Dispositivo encontrado: 192.168.1.100 - 11:22:33:44:55:66
Escaneo finalizado.
```

Este código mejora la velocidad del escaneo al paralelizar la ejecución de solicitudes ARP. 🚀  

📌 **¿Quieres agregarle detección de sistema operativo o exportar los resultados?** 🔥