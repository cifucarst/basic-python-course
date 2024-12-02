# Rebanado dentro de list comprehensions

palabras = ["Python", "es", "genial"]
rebanadas = [palabra[:2] for palabra in palabras]
print(rebanadas)  # ['Py', 'es', 'ge']


# List comprehensions con diccionarios y conjuntos

# Diccionario comprehension
numeros = [1, 2, 3, 4]
cuadrados = {n: n ** 2 for n in numeros}
print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16}


# conjunto comprehension
numeros = [1, 2, 3, 4, 4, 3]
unicos_cuadrados = {n ** 2 for n in numeros}
print(unicos_cuadrados)  # {16, 1, 9, 4}
