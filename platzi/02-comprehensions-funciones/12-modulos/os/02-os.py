# 2. os.getcwd() y os.chdir()
# os.getcwd(): Devuelve el directorio de trabajo actual.
# os.chdir(path): Cambia el directorio de trabajo a la ruta especificada.

# Ejemplo práctico: Cambiar de directorio

import os

print("Directorio actual:", os.getcwd())

nuevo_directorio = "/tmp"  # Cambia esta ruta según tu sistema
try:
    os.chdir(nuevo_directorio)
    print("Directorio cambiado a:", os.getcwd())
except FileNotFoundError:
    print(f"El directorio '{nuevo_directorio}' no existe.")