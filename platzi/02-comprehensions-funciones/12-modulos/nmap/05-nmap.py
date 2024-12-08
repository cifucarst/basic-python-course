# Ejemplo 4: Detectar el Sistema Operativo
# Utiliza la opción -O para detectar el sistema operativo (si está habilitado en el host).


import nmap

scanner = nmap.PortScanner()

# Escaneo con detección de sistema operativo
host = "192.168.0.1"
scanner.scan(hosts=host, arguments="-O")

# Mostrar el sistema operativo detectado
if "osmatch" in scanner[host]:
    print("Sistemas operativos posibles:")
    for os in scanner[host]["osmatch"]:
        print(f"  {os['name']} (probabilidad: {os['accuracy']}%)")
else:
    print("No se pudo detectar el sistema operativo.")