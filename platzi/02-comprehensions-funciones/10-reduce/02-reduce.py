from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Paso 1: Elevar al cuadrado
cuadrados = map(lambda x: x ** 2, numeros)

# Paso 2: Filtrar mayores a 10
mayores_a_diez = filter(lambda x: x > 10, cuadrados)

# Paso 3: Sumar los números
resultado = reduce(lambda x, y: x + y, mayores_a_diez)

print(resultado)  # Salida: 41 (16 + 25)