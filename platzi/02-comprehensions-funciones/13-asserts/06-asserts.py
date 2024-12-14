# Chequeo de invariantes en clases

class CuentaBancaria:
    def __init__(self, saldo):
        assert saldo >= 0, "El saldo inicial no puede ser negativo"
        self.saldo = saldo

    def retirar(self, cantidad):
        assert cantidad > 0, "La cantidad a retirar debe ser positiva"
        assert self.saldo >= cantidad, "Fondos insuficientes"
        self.saldo -= cantidad
        return self.saldo

# Prueba
cuenta = CuentaBancaria(100)
print(cuenta.retirar(30))  # Salida: 70
print(cuenta.retirar(100)) # AssertionError: Fondos insuficientes