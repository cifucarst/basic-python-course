# slicing (rebanado)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[2:6])    # [2, 3, 4, 5]
print(numeros[:4])     # [0, 1, 2, 3]
print(numeros[::2])    # [0, 2, 4, 6, 8]
print(numeros[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (lista invertida)


# Comprobar si un elemento esta en la lista
colores = ["rojo", "verde", "azul"]
print("rojo" in colores)   # True
print("amarillo" in colores)  # False


# iterar sobre una lista
nombres = ["Ana", "Luis", "Carlos"]
for nombre in nombres:
    print(nombre)


# Usando enumerate() para obtener índices y valores
for indice, valor in enumerate(nombres):
    print(f"Índice {indice}: {valor}")