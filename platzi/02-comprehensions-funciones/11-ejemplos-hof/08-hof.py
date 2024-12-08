# Ejemplo 1: Pipeline para procesamiento de datos
# Descripción:
# Implementar un pipeline que realice múltiples operaciones en una lista de números.


from functools import reduce

def pipeline(operaciones, datos):
    """
    Aplica una serie de funciones en cadena a los datos.
    """
    return reduce(lambda acc, op: op(acc), operaciones, datos)

# Definir operaciones
def filtrar_pares(datos):
    return [x for x in datos if x % 2 == 0]

def elevar_cuadrado(datos):
    return [x ** 2 for x in datos]

def calcular_promedio(datos):
    return sum(datos) / len(datos) if datos else 0

# Lista de datos y operaciones
datos = [1, 2, 3, 4, 5, 6]
operaciones = [filtrar_pares, elevar_cuadrado, calcular_promedio]

# Aplicar el pipeline
resultado = pipeline(operaciones, datos)
print(resultado)  # Salida: 20.0 (promedio de [4, 16, 36])