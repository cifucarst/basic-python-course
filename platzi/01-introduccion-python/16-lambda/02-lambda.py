# Lambdas con map()
# Ejemplo: Elevar al cuadrado una lista de números

numeros = [1, 2, 3, 4]
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))  # Salida: [1, 4, 9, 16]



# Lambdas con filter()
# Ejemplo: Filtrar números pares

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Salida: [2, 4, 6]



# Lambdas con reduce()
# Ejemplo: Multiplicar todos los números de una lista

from functools import reduce

numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # Salida: 24