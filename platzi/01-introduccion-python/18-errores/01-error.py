# Ejemplo de excepción no manejada:

numero = int("abc")  # ValueError: invalid literal for int() with base 10



# Bloques try-except

try:
    # Código que podría generar una excepción
except TipoDeExcepcion:
    # Código para manejar la excepción



# Manejo de múltiples excepciones
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")



# Capturar excepciones genéricas
try:
    resultado = 10 / 0
except:
    print("Ocurrió un error.")