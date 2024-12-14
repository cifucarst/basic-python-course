# Leer y escribir al mismo tiempo
# Usa el modo r+.


with open("archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    archivo.write("\nLínea añadida al final.")
    print(contenido)



#################################################################################

# Leer un archivo como una lista de líneas
# Usa readlines() para obtener una lista.


with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)


# Esto es útil para manipular líneas de forma individual.