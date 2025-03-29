# Ejercicio 2: Filtrar Logs Sospechosos
# Tienes un diccionario con direcciones IP y la cantidad de veces que han intentado iniciar sesión en un servidor. Usa dictionary comprehension para filtrar solo las IPs con más de 50 intentos fallidos.

# 🔹 Entrada:

# logs = {
#     "192.168.1.1": 10,
#     "10.0.0.5": 75,
#     "172.16.32.5": 150,
#     "203.0.113.99": 30,
#     "8.8.8.8": 55
# }
# 🔹 Salida esperada:


# {
#     "10.0.0.5": 75,
#     "172.16.32.5": 150,
#     "8.8.8.8": 55
# }

from typing import Dict

def find_failed_attempts(logs: Dict[str, int], umbral: int = 50) -> Dict[str, int]:
    if not isinstance(logs, dict):
        raise ValueError("Debes ingresar un diccionario con direccion ip y la cantidad de intentos fallidos")
    
    try:
        return {ip:attempt for ip, attempt in logs.items() if attempt > umbral}
    except ValueError as e:
        print(f"Error: {e}")
        return {}


logs = {
    "192.168.1.1": 10,
    "10.0.0.5": 75,
    "172.16.32.5": 150,
    "203.0.113.99": 30,
    "8.8.8.8": 55
}



failed_attempts = find_failed_attempts(logs)
print(f"\nIPs con mas de 50 intentos fallidos de loging:")
print('*' * 47)
for ip, attempt in failed_attempts.items():
    print(f"{ip.ljust(15)} ➜ {attempt} intentos❌")