# Ejercicio 3: Palabras únicas en archivos de logs
# Dado un archivo de logs, extrae todas las palabras únicas que aparecen en el archivo.

# 📌 Instrucciones:

# Crea un archivo de texto con un log simulado.
# Abre el archivo y extrae todas las palabras.
# Usa un conjunto para almacenar solo las palabras únicas.
# 🔹 Ejemplo de entrada (archivo log.txt):

# [INFO] Conexión establecida desde 192.168.1.10
# [WARNING] Intento de acceso fallido desde 10.0.0.3
# [INFO] Conexión establecida desde 192.168.1.11
# 🔹 Salida esperada:

# {"INFO", "WARNING", "Conexión", "establecida", "desde", "Intento", "de", "acceso", "fallido"}


import string

def extraer_palabras_unicas() -> set:
    """Lee un archivo de log y devuelve un conjunto de palabras únicas sin signos de puntuación."""
    palabras_unicas = set()
    
    with open('log.txt', 'r') as file:
        for linea in file:
            # Eliminar signos de puntuación y convertir a minúsculas
            linea = linea.translate(str.maketrans("", "", string.punctuation)).lower()
            palabras = linea.split()  # Divide la línea en palabras
            palabras_unicas.update(palabras)  # Agrega todas las palabras al conjunto
    
    return palabras_unicas  

resultado = extraer_palabras_unicas()
print(type(resultado))
print(resultado)