# Ejercicio 5: Longitud de palabras

# Dada una lista de palabras:

# palabras = ["python", "java", "c++", "javascript"]

# Usa comprensión de diccionarios para crear un diccionario donde las claves sean las palabras y los valores la longitud de esas palabras.

# Ejemplo esperado:

# {"python": 6, "java": 4, "c++": 3, "javascript": 10}


words = ["python", "java", "c++", "javascript"]

# Crear un diccionario donde las claves son palabras y los valores son sus longitudes
result = {i: len(i) for i in words}

print(result)