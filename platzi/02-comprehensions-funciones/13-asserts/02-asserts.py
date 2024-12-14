# 1. Verificar valores de entrada

def calcular_raiz_cuadrada(numero):
    assert numero >= 0, "El número debe ser no negativo"
    return numero ** 0.5

# Prueba
print(calcular_raiz_cuadrada(9))  # Salida: 3.0
print(calcular_raiz_cuadrada(-4)) # AssertionError: El número debe ser no negativo