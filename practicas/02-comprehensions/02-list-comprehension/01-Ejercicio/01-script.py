# Ejercicio 1: Filtrar direcciones IP privadas
# Dada una lista de direcciones IP, usa list comprehension para obtener solo las que pertenecen a rangos privados:

# 192.168.x.x
# 10.x.x.x
# 172.16.x.x - 172.31.x.x

# ips = ["192.168.1.1", "8.8.8.8", "10.0.0.1", "172.16.5.4", "172.32.1.1", "127.0.0.1"]

from typing import List

def ips_privadas(ips: List[str]) -> List:
    """Filtra solo las direcciones IP privadas de una lista."""
    return [
        ip for ip in ips
        if ip.startswith("192.168.") or ip.startswith("10.") or 
           (ip.startswith("172.") and 16 <= int(ip.split(".")[1]) <= 31)
    ]

# Lista de IPs
ips = ["192.168.1.1", "8.8.8.8", "10.0.0.1", "172.16.5.4", "172.32.1.1", "127.0.0.1"]

# Imprimir resultado
print(ips_privadas(ips))