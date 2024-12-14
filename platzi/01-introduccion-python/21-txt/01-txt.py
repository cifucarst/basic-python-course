# Trabajar con archivos .txt en Python es una tarea común y útil. Aquí tienes ejemplos prácticos que abarcan operaciones básicas:

# 1. Leer un archivo completo
# Usa el modo r (lectura).

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# Explicación:

# El archivo se abre en modo lectura (r).
# with asegura que el archivo se cierre automáticamente al terminar.



#3##################################################################################


# 2. Leer línea por línea
# Si el archivo es grande, puedes procesarlo línea a línea.


with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # Elimina saltos de línea innecesarios.