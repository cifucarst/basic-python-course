# funciones lambda
# Función lambda para sumar
suma = lambda x, y: x + y
print(suma(3, 5))  # Salida: 8



# Ejemplo avanzado: Ordenar con lambdas
productos = [("Manzana", 2.5), ("Plátano", 1.2), ("Cereza", 4.0)]
productos_ordenados = sorted(productos, key=lambda p: p[1])
print(productos_ordenados)
# Salida: [('Plátano', 1.2), ('Manzana', 2.5), ('Cereza', 4.0)]



# Ejemplos avanzados

# funcion recursiva
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Salida: 120



# funcion como argumento
def aplicar_funcion(funcion, lista):
    return [funcion(x) for x in lista]

# Función a pasar
def cuadrado(n):
    return n**2

numeros = [1, 2, 3, 4]
print(aplicar_funcion(cuadrado, numeros))  # Salida: [1, 4, 9, 16]