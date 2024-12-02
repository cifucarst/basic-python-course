# Ejemplo practico
# Crear una lista de números primos

numeros = range(2, 50)
primos = [n for n in numeros if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))]
print(primos)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
