# Ejemplo 2: Detección de Versión (-sV)
# Detecta la versión del servicio en los puertos abiertos.

import nmap

scanner = nmap.PortScanner()

# Escaneo con detección de versiones
host = "192.168.0.1"
scanner.scan(hosts=host, ports="22,80", arguments="-sV")

# Mostrar resultados de versiones
for protocolo in scanner[host].all_protocols():
    print(f"Protocolo: {protocolo}")
    for puerto, detalles in scanner[host][protocolo].items():
        print(f"  Puerto: {puerto}, Estado: {detalles['state']}, Servicio: {detalles.get('product', 'N/A')}")