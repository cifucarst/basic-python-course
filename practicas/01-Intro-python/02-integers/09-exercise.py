# Ejercicio 9: Intercambio de valores

# Crea un programa que:

#     Solicite al usuario dos números (pueden ser enteros o decimales).
#     Intercambie los valores de las variables y muestre el resultado.
#         Por ejemplo, si el usuario introduce a=5 y b=3, al final a=3 y b=5.


def obtener_numeros():
    """Solicita al usuario dos números enteros y los devuelve como una tupla."""
    while True:
        try:
            num1 = int(input("Escribe el primer número: "))
            num2 = int(input("Escribe el segundo número: "))
            return num1, num2
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa números enteros válidos.")

def intercambiar_valores(a, b):
    """Intercambia los valores de dos variables y las devuelve."""
    return b, a

def run():
    num1, num2 = obtener_numeros()
    print(f"Antes del intercambio:")
    print(f"Primer número: {num1}")
    print(f"Segundo número: {num2}")

    num1, num2 = intercambiar_valores(num1, num2)

    print(f"\nDespués del intercambio:")
    print(f"Primer número: {num1}")
    print(f"Segundo número: {num2}")

if __name__ == '__main__':
    run()