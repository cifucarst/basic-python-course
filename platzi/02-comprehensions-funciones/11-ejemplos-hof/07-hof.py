# Ejemplo 7: Componer funciones
# Descripción:
# Combinar varias funciones en una sola utilizando funciones de orden superior.


def componer(f, g):
    return lambda x: f(g(x))

# Funciones simples
def sumar_uno(x):
    return x + 1

def multiplicar_por_dos(x):
    return x * 2

# Composición de funciones
operacion_compuesta = componer(multiplicar_por_dos, sumar_uno)

print(operacion_compuesta(3))  # Salida: 8 (Primero 3+1=4, luego 4*2=8)