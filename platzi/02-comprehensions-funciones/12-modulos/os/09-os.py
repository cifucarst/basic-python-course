# 9. os.stat()
# Devuelve información detallada sobre un archivo o directorio (como tamaño, permisos, etc.).

# Ejemplo práctico: Obtener información de un archivo


import os

archivo = __file__  # Nombre del archivo actual
info = os.stat(archivo)
print(f"Tamaño del archivo '{archivo}': {info.st_size} bytes.")