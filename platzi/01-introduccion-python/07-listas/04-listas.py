# ordenar numeros
numeros = [4, 2, 9, 1, 7]
numeros.sort()
print(numeros)  # [1, 2, 4, 7, 9]


# crear una lista de cuadrados
numeros = [1, 2, 3, 4]
cuadrados = [x ** 2 for x in numeros]
print(cuadrados)  # [1, 4, 9, 16]


# filtrar elementos
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6]