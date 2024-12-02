#  Operaciones comunes con matrices
# Crear una matriz vacía o inicializada

filas, columnas = 3, 4
matriz_vacia = [[0 for _ in range(columnas)] for _ in range(filas)]
print(matriz_vacia)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# con NumPy
import numpy as np

# Matriz de ceros de 3x4
matriz_ceros = np.zeros((3, 4))
print(matriz_ceros)


