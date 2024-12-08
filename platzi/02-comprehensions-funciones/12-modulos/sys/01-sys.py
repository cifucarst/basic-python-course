import sys

# El módulo sys en Python proporciona acceso a variables y funciones específicas del 
# sistema operativo y del intérprete de Python. Este módulo es esencial para interactuar 
# con el entorno de ejecución, manejar argumentos de línea de comandos y realizar tareas 
# avanzadas como modificar el comportamiento del intérprete.


# 1. sys.argv
# Es una lista que contiene los argumentos pasados al script desde la línea de comandos. El primer elemento (sys.argv[0]) es el nombre del script.

# Ejemplo práctico: Leer argumentos desde la terminal

import sys

if len(sys.argv) > 1:
    print("Argumentos proporcionados:")
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")
else:
    print("No se proporcionaron argumentos.")

# Ejecutar desde la terminal: python3 script.py Hola Mundo
# Salida:
# Argumentos proporcionados:
# Argumento 0: script.py
# Argumento 1: Hola
# Argumento 2: Mundo