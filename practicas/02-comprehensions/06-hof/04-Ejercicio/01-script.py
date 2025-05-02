# ✅ Ejercicio 4: Simulación de escaneo de puertos con map() y socket
# 🕵️‍♂️ Contexto:
# Estás desarrollando un script de reconocimiento activo para evaluar si ciertos puertos están abiertos en un host. Esto es una técnica típica de la fase de reconocimiento activo en un pentest.

# 🧩 Instrucciones:
# Crea una función es_puerto_abierto(host: str, puerto: int) -> bool que:

# Intente conectarse al host y puerto dados usando socket.

# Devuelva True si el puerto está abierto (es decir, si la conexión fue exitosa), o False si no.

# Usa una función parcial (functools.partial) para crear una función de un solo parámetro (puerto) fijando el host.

# Usa map() para escanear una lista de puertos y ver cuáles están abiertos.

# Imprime los puertos abiertos.

# 📌 Tips técnicos:
# Usa socket.socket() con .connect_ex() para no lanzar excepciones.

# Usa un timeout bajito (0.5 segundos) para que no tarde mucho.

# 🧪 Datos de ejemplo:

# host = "127.0.0.1"
# puertos_a_probar = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]


import socket
import functools

def es_puerto_abierto(host: str, puerto: int) -> bool:
    """
    Intenta conectarse al host y puerto dados usando socket.

    Args:
        host: La dirección IP o nombre de host.
        puerto: El número de puerto a verificar.

    Returns:
        True si el puerto está abierto, False en caso contrario.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            resultado = s.connect_ex((host, puerto))
            return resultado == 0
    except socket.error as e:
        print(f"Error de socket al intentar conectar a {host}:{puerto}: {e}")
        return False

if __name__ == "__main__":
    host = "127.0.0.1"
    puertos_a_probar = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

    # Crear una función parcial que fija el host
    verificar_puerto_en_host = functools.partial(es_puerto_abierto, host)

    # Usar map() para escanear la lista de puertos
    resultados = map(verificar_puerto_en_host, puertos_a_probar)

    # Imprimir los puertos abiertos
    print(f"Escaneando puertos en el host: {host}")
    puertos_abiertos = [puerto for puerto, abierto in zip(puertos_a_probar, resultados) if abierto]

    if puertos_abiertos:
        print("Puertos abiertos encontrados:")
        for puerto in puertos_abiertos:
            print(f"- Puerto {puerto}")
    else:
        print("No se encontraron puertos abiertos en el rango especificado.")
