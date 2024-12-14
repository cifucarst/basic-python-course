# Ejemplo práctico: Contar palabras


with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    palabras = contenido.split()  # Divide el texto en palabras
    print(f"El archivo tiene {len(palabras)} palabras.")


###################################################################################

# Ejemplo práctico: Buscar una palabra específica


palabra_buscada = "Python"
with open("archivo.txt", "r") as archivo:
    for numero, linea in enumerate(archivo, start=1):
        if palabra_buscada in linea:
            print(f"Palabra encontrada en la línea {numero}: {linea.strip()}")