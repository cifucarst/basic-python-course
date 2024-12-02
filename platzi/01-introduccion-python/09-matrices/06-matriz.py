# Ejemplo práctico completo
# Representar una imagen en escala de grises

imagen = [
    [0, 128, 255],
    [64, 192, 255],
    [0, 64, 128]
]

for fila in imagen:
    print(" ".join(map(str, fila)))
# 0 128 255
# 64 192 255
# 0 64 128



# Resolver un sistema de ecuaciones lineales
# Resolver:

# 2𝑥 + 3𝑦 = 84𝑥 + 𝑦 = 102x+3y=84x+y=10
# Con NumPy:
import numpy as np

A = np.array([[2, 3], [4, 1]])  # Coeficientes
B = np.array([8, 10])           # Términos independientes

solucion = np.linalg.solve(A, B)
print(solucion)  # [1. 2.]