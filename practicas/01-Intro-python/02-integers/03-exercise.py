# Ejercicio 3: Redondeo y truncamiento

# Haz un programa que:

#     Solicite al usuario que introduzca un número decimal.
#     Muestre:
#         El número redondeado al entero más cercano.
#         El número truncado (sin decimales).
#         El número redondeado a 2 decimales.


import math

def run():
    try:
        numero = float(input('Ingresa un número decimal: '))
        
        # Redondeo al entero más cercano
        print(f"🔵 Redondeado al entero más cercano: {round(numero)}")
        
        # Redondeo a 2 decimales
        print(f"🔵 Redondeado a 2 decimales: {numero:.2f}")
        
        # Truncamiento
        print(f"🔵 Truncado (parte entera): {math.trunc(numero)}")
        
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número decimal.")

if __name__ == '__main__':
    run()


# input
# Ingresa un número decimal: 12.3456


# ouput
# 🔵 Redondeado al entero más cercano: 12
# 🔵 Redondeado a 2 decimales: 12.35
# 🔵 Truncado (parte entera): 12