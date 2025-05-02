# 4. sys.platform
# Devuelve una cadena que indica la plataforma en la que se está ejecutando Python.

# Ejemplo práctico: Detectar el sistema operativo


import sys

platform = sys.platform

if platform.startswith('win'):
    print("Estás en Windows.")
elif platform.startswith('linux'):
    print("Estás en Linux.")
elif platform.startswith('darwin'):
    print("Estás en macOS.")
else:
    print(f"Plataforma no identificada: {platform}")
