import nmap
import json  # Para formatear la salida de manera legible

# Crear el escáner
scanner = nmap.PortScanner()

# Ejecutar el escaneo con detección de versiones (-sV)
scanner.scan('192.168.0.1', '1-1000', '-sV')

# Imprimir toda la información en formato JSON legible
print(json.dumps(scanner.scaninfo(), indent=4))  # Info del escaneo
print(json.dumps(scanner.all_hosts(), indent=4))  # Hosts detectados
print(json.dumps(scanner._scan_result, indent=4))  # Resultado completo