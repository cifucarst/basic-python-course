from typing import List, Set

ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.2", "10.0.0.1"]

def obtener_ips_unicas(ips: List[str]) -> Set[str]:
    """Devuelve un conjunto de direcciones IP únicas."""
    return set(ips)

result = obtener_ips_unicas(ips)
print(result)