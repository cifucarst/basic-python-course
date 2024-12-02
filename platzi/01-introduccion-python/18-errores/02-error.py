# Usar else y finally

try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print(f"El resultado es {resultado}")
finally:
    print("Gracias por usar el programa.")



# Crear excepciones personalizadas
class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

try:
    numero = int(input("Introduce un número positivo: "))
    if numero < 0:
        raise ErrorPersonalizado("El número debe ser positivo.")
except ErrorPersonalizado as e:
    print(e.mensaje)



# Levantar excepciones con raise
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

try:
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print(e)
