from typing import Dict

def find_failed_attempts(logs: Dict[str, int], umbral: int = 50) -> Dict[str, int]:
    """
    Filtra y devuelve las IPs con más intentos fallidos que el umbral definido.
    """
    if not isinstance(logs, dict):
        raise ValueError("El parámetro 'logs' debe ser un diccionario con direcciones IP como claves y enteros como valores.")
    
    # Validar que todos los valores sean números enteros positivos
    if not all(isinstance(attempt, int) and attempt >= 0 for attempt in logs.values()):
        raise ValueError("Todos los intentos de acceso deben ser números enteros positivos.")

    return {ip: attempt for ip, attempt in logs.items() if attempt > umbral}

# Diccionario de intentos de acceso fallidos
logs = {
    "192.168.1.1": 10,
    "10.0.0.5": 75,
    "172.16.32.5": 150,
    "203.0.113.99": 30,
    "8.8.8.8": 55
}

# Filtrar intentos sospechosos
failed_attempts = find_failed_attempts(logs)

# Imprimir resultados formateados
print(f"\nIPs con más de {50} intentos fallidos de login:")
print("*" * 47)
for ip, attempt in failed_attempts.items():
    print(f"{ip.ljust(15)} ➜ {attempt} intentos ❌")