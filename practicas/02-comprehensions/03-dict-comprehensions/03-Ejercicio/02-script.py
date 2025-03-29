import datetime

def encontrar_ip_sospechosas(logs, umbral=100, archivo_log="ips_sospechosas.log"):
    """
    Devuelve un diccionario con las IPs que tienen más de 'umbral' intentos de conexión.
    También guarda el resultado en un archivo de log con timestamp.
    """
    if not isinstance(logs, dict):
        raise ValueError("El parámetro logs debe ser un diccionario de IPs con intentos de conexión.")

    ips_sospechosas = {ip: intentos for ip, intentos in logs.items() if intentos > umbral}

    # Guardar en archivo de log
    if ips_sospechosas:
        with open(archivo_log, "a") as f:
            f.write(f"\n[{datetime.datetime.now()}] - IPs sospechosas detectadas:\n")
            for ip, intentos in ips_sospechosas.items():
                f.write(f"{ip} ➜ {intentos} intentos\n")
    
    return ips_sospechosas

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

print("\nLas IPs sospechosas se han guardado en 'ips_sospechosas.log'.")
