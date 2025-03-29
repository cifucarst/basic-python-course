from typing import Dict
import datetime

def find_failed_attempts(logs: Dict[str, int], umbral: int = 50, alert_threshold: int = 100) -> Dict[str, int]:
    """
    Filtra y devuelve las IPs con más intentos fallidos que el umbral definido.
    Guarda los logs sospechosos en un archivo y envía alertas si superan el umbral de alerta.
    """
    if not isinstance(logs, dict):
        raise ValueError("El parámetro 'logs' debe ser un diccionario con direcciones IP como claves y enteros como valores.")
    
    # Validar que todos los valores sean números enteros positivos
    if not all(isinstance(attempt, int) and attempt >= 0 for attempt in logs.values()):
        raise ValueError("Todos los intentos de acceso deben ser números enteros positivos.")

    # Filtrar intentos sospechosos
    filtered_logs = {ip: attempt for ip, attempt in logs.items() if attempt > umbral}

    # Guardar en archivo
    save_to_file(filtered_logs)

    # Enviar alerta si alguna IP supera el umbral de alerta
    for ip, attempt in filtered_logs.items():
        if attempt > alert_threshold:
            print(f"⚠️ ALERTA: La IP {ip} ha intentado acceder {attempt} veces. ¡Posible ataque de fuerza bruta! 🚨")

    return filtered_logs

def save_to_file(filtered_logs: Dict[str, int]):
    """Guarda las IPs sospechosas en un archivo de texto."""
    with open("logs_sospechosos.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n[{timestamp}] Logs sospechosos detectados:\n")
        for ip, attempt in filtered_logs.items():
            file.write(f"{ip} ➜ {attempt} intentos\n")
    print("✅ Logs sospechosos guardados en 'logs_sospechosos.txt'.")

# Diccionario de intentos de acceso fallidos
logs = {
    "192.168.1.1": 10,
    "10.0.0.5": 75,
    "172.16.32.5": 150,
    "203.0.113.99": 30,
    "8.8.8.8": 55,
    "45.33.22.11": 120  # Esta debería generar una alerta
}

# Filtrar intentos sospechosos
failed_attempts = find_failed_attempts(logs)

# Imprimir resultados formateados
print(f"\nIPs con más de {50} intentos fallidos de login:")
print("*" * 47)
for ip, attempt in failed_attempts.items():
    print(f"{ip.ljust(15)} ➜ {attempt} intentos ❌")