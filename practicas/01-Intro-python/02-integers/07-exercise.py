# Ejercicio 7: Conversión de temperaturas

# Crea un programa que:

#     Solicite al usuario una temperatura en grados Celsius (puede ser decimal).
#     Convierta esa temperatura a Fahrenheit usando la fórmula:
#     F=(C×95)+32
#     F=(C×59​)+32
#     Muestra el resultado con 2 decimales.


def convertir_celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def run():
    print("🌡️ Conversor de temperaturas 🌡️\n")
    try:
        # Solicitar temperatura en Celsius
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        
        # Convertir a Fahrenheit
        fahrenheit = convertir_celsius_a_fahrenheit(celsius)

        # Mostrar resultado
        print(f"\n✅ {celsius:.2f} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")
    
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número válido.")


if __name__ == "__main__":
    run()