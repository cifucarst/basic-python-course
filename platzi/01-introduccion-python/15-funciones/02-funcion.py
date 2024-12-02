# Parámetros arbitrarios
# *args: Recoge argumentos posicionales como una tupla.
# **kwargs: Recoge argumentos nombrados como un diccionario.

# *args
def sumar_todos(*args):
    return sum(args)

print(sumar_todos(1, 2, 3, 4))  # Salida: 10

# **kwargs
def informacion(**kwargs):
    return kwargs

print(informacion(nombre="Ana", edad=22, ciudad="Bogotá"))
# Salida: {'nombre': 'Ana', 'edad': 22, 'ciudad': 'Bogotá'}



# Retorno de valores
# Ejemplo basico
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print(resultado)  # Salida: 20



# Retorno multiple
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b

suma, resta, producto, division = operaciones_basicas(10, 2)
print(suma, resta, producto, division)
# Salida: 12 8 20 5.0
