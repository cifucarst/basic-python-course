# Métodos de las tuplas

# count()
mi_tupla = (1, 2, 3, 2, 2, 4)
print(mi_tupla.count(2))  # 3


# index()
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla.index(3))  # 2


# Usos comunes de las tuplas
# Retornar múltiples valores de una función

def operaciones(a, b):
    suma = a + b
    producto = a * b
    return suma, producto

resultado = operaciones(3, 5)
print(resultado)  # (8, 15)

# Desempaquetar los resultados
suma, producto = operaciones(3, 5)
print(suma, producto)  # 8 15


# llaves en diccionarios
coordenadas = {(0, 0): "origen", (1, 2): "punto A"}
print(coordenadas[(1, 2)])  # "punto A"


# Almacenar datos constantes
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print(dias_semana[0])  # "lunes"
