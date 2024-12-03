# sintaxis basica
# {clave: valor for elemento in iterable}

# Ejemplos básicos
# Crear un diccionario a partir de un rango

# Diccionario donde la clave es un número y el valor es su cuadrado
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



#  Convertir una lista en un diccionario
# Crear un diccionario con palabras como claves y su longitud como valor
palabras = ["Python", "Programación", "Avanzado"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(longitudes)  
# Salida: {'Python': 6, 'Programación': 12, 'Avanzado': 8}



# Filtrar elementos en el diccionario
# Diccionario con solo los números pares y sus cuadrados
pares_cuadrados = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares_cuadrados)  
# Salida: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}



# Añadiendo condiciones con if-else
# Clasificar números como "par" o "impar"
clasificacion = {x: "par" if x % 2 == 0 else "impar" for x in range(5)}
print(clasificacion)  
# Salida: {0: 'par', 1: 'impar', 2: 'par', 3: 'impar', 4: 'par'}