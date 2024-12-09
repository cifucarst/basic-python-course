# 3. deque (Double-Ended Queue)
# Es una cola doblemente terminada que permite agregar y eliminar elementos desde ambos extremos de manera eficiente.

# Ejemplo: Implementar una cola

from collections import deque

cola = deque()

# Agregar elementos
cola.append("A")
cola.append("B")
cola.appendleft("C")  # Agregar al inicio
print(cola)  # Salida: deque(['C', 'A', 'B'])

# Eliminar elementos
cola.pop()  # Eliminar desde el final
cola.popleft()  # Eliminar desde el inicio
print(cola)  # Salida: deque(['A'])