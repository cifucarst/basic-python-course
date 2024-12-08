# 7. sys.getsizeof()
# Devuelve el tamaño en bytes de un objeto en memoria.

# Ejemplo práctico: Medir el tamaño de diferentes objetos


import sys

a = 10
b = [1, 2, 3]
c = "Hola, mundo"

print(f"El tamaño de 'a' es: {sys.getsizeof(a)} bytes.")
print(f"El tamaño de 'b' es: {sys.getsizeof(b)} bytes.")
print(f"El tamaño de 'c' es: {sys.getsizeof(c)} bytes.")