# Ejercicio 3: Filtrado de Direcciones IP Sospechosas
# 📌 Objetivo: Dado un diccionario de direcciones IP y sus intentos de conexión, usa dictionary comprehension para quedarte solo con las IPs sospechosas (más de 100 intentos).

# 🔹 Instrucciones:
# Dado este diccionario de intentos de conexión:

# intentos = {
#     "192.168.1.10": 50,
#     "10.0.0.5": 200,
#     "172.16.5.1": 10,
#     "203.0.113.99": 150,
#     "8.8.8.8": 5
# }
# Usa dictionary comprehension para quedarte solo con las IPs con más de 100 intentos.

# 📌 Salida esperada:

# {
#     "10.0.0.5": 200,
#     "203.0.113.99": 150
# }


def encontrar_ip_sospechosas(logs):
    """
    Devuelve un diccionario con las IPs que tienen más de 100 intentos de conexión.
    """
    if not isinstance(logs, dict):
        raise ValueError("El parámetro logs debe ser un diccionario de IPs con intentos de conexión.")
    
    return {ip: intento for ip, intento in logs.items() if intento > 100}

# Diccionario de intentos de conexión
intentos = {
    "192.168.1.10": 50,
    "10.0.0.5": 200,
    "172.16.5.1": 10,
    "203.0.113.99": 150,
    "8.8.8.8": 5
}

# Obtener resultado y mostrarlo formateado
resultado = encontrar_ip_sospechosas(intentos)

print("\nIPs sospechosas detectadas:")
print("-" * 30)
for ip, intentos in resultado.items():
    print(f"{ip.ljust(15)} ➜ {intentos} intentos")
