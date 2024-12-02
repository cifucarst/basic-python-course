# Ejemplos avanzados

# Usar una función en la expresión
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = [cuadrado(n) for n in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]


# anidar bucles
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
pares = [(letra, numero) for letra in letras for numero in numeros]
print(pares)
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
