# Ejercicio 10: Promedio de números

# Haz un programa que:

#     Solicite al usuario que introduzca 5 números (pueden ser enteros o decimales).
#     Calcule y muestre el promedio de esos números.

def calcular_promedio(cantidad=5):
    """Calcula el promedio de una cantidad dada de números ingresados por el usuario.

    Args:
        cantidad (int): La cantidad de números a promediar. Por defecto, 5.

    Returns:
        None
    """
    numeros = []
    print(f"Por favor, ingresa {cantidad} números para calcular el promedio.")

    for i in range(cantidad):
        while True:
            try:
                numero = float(input(f"Ingrese el número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("❌ Entrada inválida. Por favor, ingresa un número válido.")

    promedio = sum(numeros) / len(numeros)
    print(f"\n✅ El promedio de los números ingresados es: {promedio:.2f}")

if __name__ == "__main__":
    calcular_promedio()