# Ejercicio 4: Conversión de unidades

# Crea un programa que:

#     Solicite al usuario un valor en kilómetros.
#     Convierta ese valor a metros y millas.
#         1 kilómetro = 1000 metros.
#         1 kilómetro = 0.621371 millas.
#     Muestra los resultados con 2 decimales.

def convertir_a_metros(kilometros):
    """Convierte kilómetros a metros."""
    return kilometros * 1000

def convertir_a_millas(kilometros):
    """Convierte kilómetros a millas."""
    return kilometros * 0.621371

def run():
    try:
        # Solicitar al usuario el valor en kilómetros
        kilometros = float(input("Ingrese la cantidad de kilómetros (en unidades positivas): "))
        
        if kilometros <= 0:
            print("❌ Los kilómetros deben ser un número positivo. Inténtalo nuevamente.")
            return
        
        # Opciones de conversión
        print("\n🔄 Opciones de conversión:")
        print("1. Convertir a metros")
        print("2. Convertir a millas")
        print("3. Convertir a ambas unidades")

        opcion = int(input("\nSelecciona una opción (1, 2 o 3): "))

        if opcion == 1:
            metros = convertir_a_metros(kilometros)
            print(f"\n✅ Resultado: {kilometros} kilómetros son {metros} metros.")
        elif opcion == 2:
            millas = convertir_a_millas(kilometros)
            print(f"\n✅ Resultado: {kilometros} kilómetros son {millas:.3f} millas.")
        elif opcion == 3:
            metros = convertir_a_metros(kilometros)
            millas = convertir_a_millas(kilometros)
            print(f"\n✅ Resultados:")
            print(f"{kilometros} kilómetros son {metros} metros.")
            print(f"{kilometros} kilómetros son {millas:.3f} millas.")
        else:
            print("❌ Opción inválida. Por favor, selecciona 1, 2 o 3.")
    
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número válido.")

if __name__ == "__main__":
    run()