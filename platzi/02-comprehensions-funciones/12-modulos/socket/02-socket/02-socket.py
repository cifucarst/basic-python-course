import socket

def scan_ports(host, ports):
    print(f"Escaneando {host}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Tiempo límite para cada intento
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Puerto {port} está ABIERTO")
        else:
            print(f"Puerto {port} está CERRADO")
        sock.close()

# Prueba con un rango de puertos
scan_ports('127.0.0.1', range(20, 1025))