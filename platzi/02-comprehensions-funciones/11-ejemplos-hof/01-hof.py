# Ejemplo 1: Crear una función personalizada que tome otra función como argumento
# Descripción:
# Una función de orden superior que aplica una operación específica a cada elemento de una lista.

def aplicar_operacion(lista, operacion):
    return [operacion(x) for x in lista]

# Operaciones definidas
def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

numeros = [1, 2, 3, 4]

# Aplicar las operaciones
print(aplicar_operacion(numeros, cuadrado))  # Salida: [1, 4, 9, 16]
print(aplicar_operacion(numeros, cubo))     # Salida: [1, 8, 27, 64]