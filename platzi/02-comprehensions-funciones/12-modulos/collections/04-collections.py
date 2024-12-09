# 4. namedtuple
# Crea una clase de tupla con nombre, lo que permite acceder a los elementos mediante atributos además de índices.

# Ejemplo: Representar puntos en 2D


from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])
p = Punto(10, 20)

print(p.x, p.y)  # Salida: 10 20
print(p)  # Salida: Punto(x=10, y=20)

# Convertir a diccionario
print(p._asdict())  # Salida: {'x': 10, 'y': 20}