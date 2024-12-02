# apliccaciones practicas

# validacion de un usuario
usuario = input("Introduce tu nombre: ").strip()
if usuario:
    print(f"Hola, {usuario}!")
else:
    print("No ingresaste tu nombre.")


# verificar si un numero es divisible entre otro
def es_divisible(a, b):
    return b != 0 and a % b == 0

print(es_divisible(10, 2))  # True
print(es_divisible(10, 3))  # False


# condiciones con listas no vacias
elementos = [1, 2, 3]
if elementos:
    print("La lista tiene elementos.")
else:
    print("La lista está vacía.")