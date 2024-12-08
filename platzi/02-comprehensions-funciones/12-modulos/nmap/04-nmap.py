# Ejemplo 3: Escaneo de Red Completa
# Escanea una red completa utilizando un rango de direcciones IP.

import nmap

scanner = nmap.PortScanner()

# Escaneo de la red
red = "192.168.0.0/24"
scanner.scan(hosts=red, arguments="-sn")  # Escaneo sin puertos (-sn)

# Mostrar hosts activos
print("Hosts activos:")
for host in scanner.all_hosts():
    estado = scanner[host].state()
    print(f"  {host} - {estado}")