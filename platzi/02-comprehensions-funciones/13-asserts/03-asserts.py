#  Validar estado interno de una función

def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero"
    return a / b

# Prueba
print(dividir(10, 2))  # Salida: 5.0
print(dividir(10, 0))  # AssertionError: El divisor no puede ser cero