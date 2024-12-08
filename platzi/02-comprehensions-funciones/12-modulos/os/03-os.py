# 3. os.listdir()
# Devuelve una lista con los nombres de los archivos y directorios en un directorio especificado.

# Ejemplo práctico: Listar archivos en un directorio


import os

directorio = "."  # Directorio actual
print(f"Contenido de '{directorio}':")
for item in os.listdir(directorio):
    print(item)