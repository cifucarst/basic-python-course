# lambda parámetros: expresión

# Ejemplo basico
suma = lambda x, y: x + y
print(suma(3, 5))  # Salida: 8



# diferencias entre def y lambda
def cuadrado(x):
    return x ** 2

print(cuadrado(4))  # Salida: 16

# la misma funcion con lambda
cuadrado = lambda x: x ** 2
print(cuadrado(4))  # Salida: 16



# Usos básicos de lambdas
# Función lambda como argumento
# Ejemplo: Ordenar una lista de tuplas por el segundo elemento

productos = [("Manzana", 2.5), ("Plátano", 1.2), ("Cereza", 4.0)]
productos_ordenados = sorted(productos, key=lambda p: p[1])
print(productos_ordenados)
# Salida: [('Plátano', 1.2), ('Manzana', 2.5), ('Cereza', 4.0)]