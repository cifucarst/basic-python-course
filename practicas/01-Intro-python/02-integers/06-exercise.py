# Ejercicio 6: Números pares e impares

# Escribe un programa que:

#     Solicite al usuario un número entero.
#     Determine si el número es par o impar.
#     Muestra un mensaje indicando si es par o impar.


def es_par(numero):
    """Verifica si un número es par."""
    return numero % 2 == 0


def run():
    print("🔢 Comprobador de números pares e impares 🔢\n")
    try:
        numero = int(input("Por favor, ingresa un número entero: "))

        # Determinar paridad
        if es_par(numero):
            resultado_paridad = "par"
        else:
            resultado_paridad = "impar"

        # Determinar si es positivo, negativo o cero
        if numero > 0:
            signo = "positivo"
        elif numero < 0:
            signo = "negativo"
        else:
            signo = "cero"

        # Mostrar resultados
        print(f"\n✅ Resultado: El número {numero} es {resultado_paridad} y {signo}.")

    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número entero válido.")


if __name__ == "__main__":
    run()