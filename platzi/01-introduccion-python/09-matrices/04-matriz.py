# Operaciones matemáticas básicas
# Suma de matrices

# con listas
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Suma de matrices
resultado = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(resultado)  # [[6, 8], [10, 12]]


# con NumPy
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

resultado = A + B
print(resultado)  # [[6, 8], [10, 12]]


# Multiplicación escalar

A = [[1, 2], [3, 4]]
escalar = 3

resultado = [[escalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(resultado)  # [[3, 6], [9, 12]]


# con NumPy
A = np.array([[1, 2], [3, 4]])
resultado = A * 3
print(resultado)  # [[3, 6], [9, 12]]

