# Ejemplo 5: Función para generar operaciones matemáticas
# Descripción:
# Una función que devuelve otras funciones para realizar cálculos.

def generar_operacion(operador):
    if operador == "suma":
        return lambda a, b: a + b
    elif operador == "resta":
        return lambda a, b: a - b
    elif operador == "multiplicacion":
        return lambda a, b: a * b
    elif operador == "division":
        return lambda a, b: a / b
    else:
        raise ValueError("Operador no soportado")

# Crear operaciones
suma = generar_operacion("suma")
resta = generar_operacion("resta")

print(suma(10, 5))  # Salida: 15
print(resta(10, 5)) # Salida: 5