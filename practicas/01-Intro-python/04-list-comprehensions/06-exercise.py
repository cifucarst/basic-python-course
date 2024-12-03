# Ejercicio 6: Sumar listas

# Dadas las listas:

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

# Genera una lista que contenga la suma de los elementos correspondientes de lista1 y 
# lista2 usando una comprensión de lista.

# Sumar elementos correspondientes de dos listas
total = [i + j for i, j in zip(lista1, lista2)]
print(total)

# pares = [(letra, numero) for letra in letras for numero in numeros]
