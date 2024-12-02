# Representación de matrices en Python
# Matriz como lista de listas

# Matriz 2x3 (2 filas y 3 columnas)
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[0])  # Primera fila: [1, 2, 3]
print(matriz[1][2])  # Elemento de la segunda fila, tercera columna: 6


# Uso de la biblioteca NumPy
import numpy as np

# Crear una matriz 2x3 con NumPy
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
