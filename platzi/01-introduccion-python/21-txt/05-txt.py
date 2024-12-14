# Eliminar líneas específicas
# Supongamos que quieres eliminar líneas que contengan la palabra "borrar".


with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()

with open("archivo.txt", "w") as archivo:
    for linea in lineas:
        if "borrar" not in linea:
            archivo.write(linea)



# Consejos adicionales
# Manejo de errores: Usa try y except para manejar errores si el archivo no existe.
# Archivos grandes: Procesa archivos línea por línea para evitar consumir demasiada memoria.
# Codificación: Especifica la codificación con encoding="utf-8" si trabajas con caracteres especiales:


with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()