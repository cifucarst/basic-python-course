# El módulo os en Python proporciona funciones para interactuar con el sistema operativo. 
# Este módulo es útil para manejar directorios, archivos y realizar operaciones 
# relacionadas con el sistema, como obtener información del entorno, ejecutar comandos 
# del sistema o cambiar permisos de archivos.


# 1. os.name
# Devuelve el nombre del sistema operativo. Los valores comunes son:

# 'posix': Linux, macOS, etc.
# 'nt': Windows.
# Ejemplo práctico: Detectar el sistema operativo

import os

if os.name == 'posix':
    print("Estás usando un sistema basado en Unix (Linux o macOS).")
elif os.name == 'nt':
    print("Estás usando Windows.")
else:
    print(f"Sistema no identificado: {os.name}")
