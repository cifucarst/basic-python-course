# 10. os.walk()
# Permite recorrer un directorio y todos sus subdirectorios.

# Ejemplo práctico: Recorrer un directorio y sus subdirectorios


import os

directorio = "."  # Directorio actual
for raiz, directorios, archivos in os.walk(directorio):
    print(f"Directorio: {raiz}")
    for d in directorios:
        print(f"  Subdirectorio: {d}")
    for f in archivos:
        print(f"  Archivo: {f}")