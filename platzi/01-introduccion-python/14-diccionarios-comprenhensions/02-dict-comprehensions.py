# Ejemplos avanzados
# Invertir claves y valores de un diccionario

# Invertir un diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(invertido)  
# Salida: {1: 'a', 2: 'b', 3: 'c'}



# Crear un diccionario a partir de dos listas
# Usar dos listas para generar un diccionario
claves = ["nombre", "edad", "ciudad"]
valores = ["Andrés", 25, "Bogotá"]

diccionario = {clave: valor for clave, valor in zip(claves, valores)}
print(diccionario)  
# Salida: {'nombre': 'Andrés', 'edad': 25, 'ciudad': 'Bogotá'}



# Contar la frecuencia de caracteres en una cadena
cadena = "programacion"
frecuencia = {letra: cadena.count(letra) for letra in set(cadena)}
print(frecuencia)
# Salida (puede variar en orden): {'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 2, 'm': 1, 'c': 1, 'i': 1, 'n': 1}