# Ejercicio 8: Diccionario de listas

# Dada una lista de números:

# numeros = [1, 2, 3, 4, 5]

# Usa comprensión de diccionarios para crear un diccionario donde las claves sean los números y los valores sean listas con los múltiplos de ese número hasta 10.

# Ejemplo esperado:

# {
#     1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
#     ...
# }


numeros = [1, 2, 3, 4, 5]

# Crear un diccionario donde cada número tiene una lista de sus múltiplos hasta el décimo
resultado = {num: [i for i in range(num, num * 11, num)] for num in numeros}

print(resultado)