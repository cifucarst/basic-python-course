# Filtrar y transformar simultáneamente

#  Filtrar y calcular cuadrados de números pares
numeros = [1, 2, 3, 4, 5, 6]
pares_cuadrados = [n ** 2 for n in numeros if n % 2 == 0]
print(pares_cuadrados)  # [4, 16, 36]


# Ignorar elementos usando una condición
numeros = [-3, -2, -1, 0, 1, 2, 3]
positivos = [n for n in numeros if n >= 0]
print(positivos)  # [0, 1, 2, 3]
