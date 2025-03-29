# Ejercicio 4: Comparar puertos abiertos en diferentes escaneos
# Imagina que realizaste dos escaneos de puertos en un servidor usando Nmap en diferentes momentos. Escribe un programa que te ayude a encontrar:

# Puertos que estaban abiertos en el primer escaneo pero cerrados en el segundo.
# Puertos nuevos que se abrieron en el segundo escaneo.
# Puertos que se mantuvieron abiertos en ambos escaneos.
# 📌 Instrucciones:

# Define dos conjuntos de números de puertos abiertos en cada escaneo.
# Encuentra los puertos cerrados, nuevos y persistentes usando operaciones con conjuntos.
# 🔹 Ejemplo de entrada:

# escaneo1 = {22, 80, 443, 3306}
# escaneo2 = {80, 443, 8080}
# 🔹 Salida esperada:

# Puertos cerrados: {22, 3306}
# Puertos nuevos: {8080}
# Puertos persistentes: {80, 443}

from typing import Set

def analizar_cambios_puertos(escaneo1: Set[int], escaneo2: Set[int]) -> None:
    """Compara dos escaneos de puertos y muestra los cambios detectados."""
    puertos_cerrados = escaneo1 - escaneo2  # Puertos que estaban abiertos y ahora están cerrados
    puertos_nuevos = escaneo2 - escaneo1  # Puertos que se abrieron en el nuevo escaneo
    puertos_persistentes = escaneo1 & escaneo2  # Puertos que se mantuvieron abiertos

    print(f"Puertos cerrados: {puertos_cerrados}")
    print(f"Puertos nuevos: {puertos_nuevos}")
    print(f"Puertos persistentes: {puertos_persistentes}")

# Datos de los escaneos
escaneo1 = {22, 80, 443, 3306}
escaneo2 = {80, 443, 8080}

# Llamar a la función
analizar_cambios_puertos(escaneo1, escaneo2)