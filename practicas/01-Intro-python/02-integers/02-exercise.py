# Ejercicio 2: Cálculo del área y perímetro de un círculo

# Escribe un programa que:

#     Solicite al usuario que introduzca el radio de un círculo (puede ser un número decimal).
#     Calcule el área y el perímetro del círculo.
#         Área: πr2πr2
#         Perímetro: 2πr2πr
#     Muestra los resultados con 2 decimales. Usa el valor de ππ de math.pi.

import math

def calcular_area(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio**2

def calcular_perimetro(radio):
    """Calcula el perímetro de un círculo dado su radio."""
    return 2 * math.pi * radio

def run():
    try:
        # Solicitar al usuario el radio
        radio = float(input("Ingrese el radio del círculo (en unidades positivas): "))
        
        if radio <= 0:
            print("❌ El radio debe ser un número positivo. Inténtalo nuevamente.")
            return
        
        # Calcular el área y el perímetro
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)

        # Mostrar los resultados con 2 decimales
        print(f"\n✅ Resultados:")
        print(f"El área del círculo es: {area:.2f} unidades cuadradas.")
        print(f"El perímetro del círculo es: {perimetro:.2f} unidades lineales.")
    
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número.")

if __name__ == "__main__":
    run()


# ejemplo de uso
# Ingrese el radio del círculo (en unidades positivas): 5

#salida:
# ✅ Resultados:
# El área del círculo es: 78.54 unidades cuadradas.
# El perímetro del círculo es: 31.42 unidades lineales.