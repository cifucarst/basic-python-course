# Ejercicio 8: División y módulo

# Escribe un programa que:

#     Solicite al usuario dos números enteros.
#     Calcule y muestre:
#         El cociente entero de la división.
#         El resto de la división.


def calcular_cociente(num1, num2):
    """Calcula el cociente entero de una división."""
    return num1 // num2


def calcular_resto(num1, num2):
    """Calcula el resto (módulo) de una división."""
    return num1 % num2


def obtener_numeros():
    """Solicita al usuario dos números válidos para realizar cálculos."""
    while True:
        try:
            num1 = float(input("Escribe el primer número: "))
            num2 = float(input("Escribe el segundo número (no puede ser cero): "))
            if num2 == 0:
                print("❌ El divisor no puede ser cero. Inténtalo nuevamente.")
                continue
            return num1, num2
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa números válidos.")


def run():
    print("🧮 Calculadora de cociente y resto 🧮\n")
    num1, num2 = obtener_numeros()

    cociente = calcular_cociente(num1, num2)
    resto = calcular_resto(num1, num2)

    print(f"\n✅ Resultados:")
    print(f"- El cociente entero de {num1} dividido por {num2} es: {cociente}")
    print(f"- El resto de {num1} dividido por {num2} es: {resto}")


if __name__ == "__main__":
    run()