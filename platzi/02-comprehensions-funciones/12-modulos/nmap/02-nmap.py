#  Ejemplo 1: Escaneo Básico
# Escanea los puertos de un host específico.


import nmap

scanner = nmap.PortScanner()

# Escanear un host
host = "192.168.0.1"
scanner.scan(hosts=host, ports="1-100", arguments="-sS")

# Mostrar resultados
print(f"Resultados del escaneo para {host}:")
for protocolo in scanner[host].all_protocols():
    print(f"Protocolo: {protocolo}")
    puertos = scanner[host][protocolo].keys()
    for puerto in puertos:
        estado = scanner[host][protocolo][puerto]['state']
        print(f"  Puerto: {puerto}, Estado: {estado}")