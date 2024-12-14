#  Uso en pruebas automatizadas
# assert también se usa comúnmente en pruebas para garantizar que una función devuelva los resultados esperados.

def sumar(a, b):
    return a + b

# Pruebas
assert sumar(2, 3) == 5, "La suma de 2 y 3 debería ser 5"
assert sumar(-1, 1) == 0, "La suma de -1 y 1 debería ser 0"
assert sumar(0, 0) == 0, "La suma de 0 y 0 debería ser 0"
print("Todas las pruebas pasaron")