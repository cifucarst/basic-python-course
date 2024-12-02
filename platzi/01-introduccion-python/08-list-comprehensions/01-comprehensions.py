# List Comprehensions

# [expresión for elemento in iterable if condición]

# crear una lista de numeros al cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]


# Filtrar numero pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4, 6, 8]


# convertir cadenas a mayusculas
palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['HOLA', 'MUNDO', 'PYTHON']