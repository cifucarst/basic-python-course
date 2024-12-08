# Ejemplo 6: Simulación de operaciones bancarias
# Descripción:
# Un sistema que aplica diferentes funciones para simular operaciones bancarias.


def depositar(cuenta, monto):
    cuenta["saldo"] += monto
    return cuenta

def retirar(cuenta, monto):
    if cuenta["saldo"] >= monto:
        cuenta["saldo"] -= monto
    else:
        raise ValueError("Saldo insuficiente")
    return cuenta

def aplicar_interes(cuenta, tasa):
    cuenta["saldo"] *= (1 + tasa)
    return cuenta

# Pipeline para operaciones bancarias
def ejecutar_operaciones(cuenta, operaciones):
    for operacion in operaciones:
        cuenta = operacion(cuenta)
    return cuenta

# Crear cuenta y operaciones
cuenta = {"saldo": 1000}
operaciones = [
    lambda c: depositar(c, 500),
    lambda c: retirar(c, 200),
    lambda c: aplicar_interes(c, 0.05),
]

resultado = ejecutar_operaciones(cuenta, operaciones)
print(resultado)  # Salida: {'saldo': 1365.0}