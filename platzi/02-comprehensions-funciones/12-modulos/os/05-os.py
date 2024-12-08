# 5. os.remove() y os.rename()
# os.remove(path): Elimina un archivo.
# os.rename(src, dst): Renombra un archivo o directorio.

# Ejemplo práctico: Renombrar y eliminar un archivo


import os

archivo = "ejemplo.txt"

# Crear un archivo para la demostración
with open(archivo, "w") as f:
    f.write("Hola, este es un archivo temporal.")

# Renombrar el archivo
nuevo_nombre = "archivo_renombrado.txt"
os.rename(archivo, nuevo_nombre)
print(f"Archivo renombrado a '{nuevo_nombre}'.")

# Eliminar el archivo
os.remove(nuevo_nombre)
print(f"Archivo '{nuevo_nombre}' eliminado.")