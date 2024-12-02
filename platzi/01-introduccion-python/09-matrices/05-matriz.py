# Multiplicación de matrices

# con listas
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print(resultado)  # [[19, 22], [43, 50]]


# con NumPy
import NumPy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

resultado = np.dot(A, B)
print(resultado)  # [[19, 22], [43, 50]]


