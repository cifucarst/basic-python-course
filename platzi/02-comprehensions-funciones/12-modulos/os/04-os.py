# 4. os.makedirs() y os.rmdir()
# os.makedirs(path): Crea un directorio, incluyendo cualquier subdirectorio necesario.
# os.rmdir(path): Elimina un directorio vacío.

# Ejemplo práctico: Crear y eliminar un directorio

import os

directorio = "mi_directorio"
os.makedirs(directorio, exist_ok=True)
print(f"Directorio '{directorio}' creado.")

os.rmdir(directorio)
print(f"Directorio '{directorio}' eliminado.")