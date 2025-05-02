# ✅ Ejercicio 1: Filtrar IPs maliciosas usando filter
# Contexto: Tienes una lista de direcciones IP, algunas de ellas están en una lista negra (blacklist). Necesitas filtrar solo las IPs maliciosas.

# Instrucciones:
# Crea una función llamada es_maliciosa(ip) que reciba una IP y devuelva True si está en la lista negra.

# Usa filter() y es_maliciosa() para obtener todas las IPs maliciosas de una lista de tráfico.

# Imprime la lista de IPs maliciosas detectadas.

# Datos de ejemplo:

# blacklist = {"192.168.1.10", "10.0.0.5", "172.16.0.9"}
# trafico = [
#     "192.168.1.10", "192.168.1.15", "10.0.0.1", 
#     "10.0.0.5", "172.16.0.9", "8.8.8.8"
# ]


from typing import Set, List

def es_maliciosa(blacklist: Set[str], trafico: List[str]) -> List[str]:
    if not isinstance(blacklist, set):
        raise ValueError("El parámetro 'blacklist' debe ser un conjunto de IPs.")
    
    if not isinstance(trafico, list):
        raise ValueError("El parámetro 'trafico' debe ser una lista de IPs.")
    
    if not all(isinstance(ip, str) for ip in blacklist | set(trafico)):
        raise ValueError("Todas las IPs deben ser strings.")

    return list(filter(lambda ip: ip in blacklist, trafico))



blacklist = {"192.168.1.10", "10.0.0.5", "172.16.0.9"}

trafico = [
    "192.168.1.10", "192.168.1.15", "10.0.0.1", 
    "10.0.0.5", "172.16.0.9", "8.8.8.8"
]

result = es_maliciosa(blacklist, trafico)
print(result)