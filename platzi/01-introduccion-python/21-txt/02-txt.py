# Escribir en un archivo
# Usa el modo w (escritura). Este borra el contenido previo del archivo.


with open("archivo.txt", "w") as archivo:
    archivo.write("Primera línea.\n")
    archivo.write("Segunda línea.\n")


# Nota: Si el archivo no existe, Python lo crea.


############################################################################

# Agregar contenido a un archivo existente
# Usa el modo a (agregar).


with open("archivo.txt", "a") as archivo:
    archivo.write("Nueva línea agregada.\n")