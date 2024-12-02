# Controlar errores en la entrada

try:
    numero = int(input("Introduce un número entero: "))
    print(f"El doble de tu número es {numero * 2}.")
except ValueError:
    print("Error: Debes ingresar un número entero.")


# Combinando input con condiciones
respuesta = input("¿Quieres continuar? (sí/no): ").lower()

if respuesta == "sí":
    print("Continuamos...")
elif respuesta == "no":
    print("Hasta luego.")
else:
    print("Respuesta no válida.")


# personalizar la entrada
valores = input("Introduce tres números separados por comas: ").split(',')
numeros = [int(valor) for valor in valores]
print(f"La suma de los números es {sum(numeros)}.")


# funciones relacionadas
usuario = input("Escribe tu nombre: ").strip().lower()
print(f"Hola, {usuario}!")