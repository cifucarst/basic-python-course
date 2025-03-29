# Ejercicio 5: Filtrar logs con errores
# Dada una lista de registros de logs, usa list comprehension para extraer solo los que contienen la palabra "ERROR".


# logs = [
#     "[INFO] Connection established",
#     "[ERROR] Failed login attempt",
#     "[WARNING] High CPU usage detected",
#     "[ERROR] Firewall rule misconfiguration"
# ]

from typing import List

def extract_errors(logs: List[str]) -> List[str]:
    return [error for error in logs if  "[ERROR]" in error]

logs = [
    "[INFO] Connection established",
    "[ERROR] Failed login attempt",
    "[WARNING] High CPU usage detected",
    "[ERROR] Firewall rule misconfiguration"
]

result = extract_errors(logs)
print(result)