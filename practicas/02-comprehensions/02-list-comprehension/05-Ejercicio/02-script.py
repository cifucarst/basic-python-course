from typing import List

def extract_errors(logs: List[str]) -> List[str]:
    """Extrae solo los mensajes de error de un registro de logs."""
    return [log for log in logs if "[error]" in log.lower()]

# Lista de logs
logs = [
    "[INFO] Connection established",
    "[ERROR] Failed login attempt",
    "[WARNING] High CPU usage detected",
    "[ERROR] Firewall rule misconfiguration"
]

# Obtener errores
result = extract_errors(logs)

# Mostrar resultado
print("\n".join(result))