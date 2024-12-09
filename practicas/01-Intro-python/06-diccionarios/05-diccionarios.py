# Ejercicio 5: Diccionario de cuadrados

# Escribe un programa que genere un diccionario donde las claves sean números enteros del 1 al 10 y los valores sean sus cuadrados.

# Ejemplo:

# salida = {1: 1, 2: 4, 3: 9, ..., 10: 100}

def squares_dictionary():
    """
    Genera un diccionario donde las claves son números del 1 al 10
    y los valores son los cuadrados de esas claves.
    """
    new_dict = {}
    for i in range(1, 11):
        new_dict[i] = i ** 2  # Calcula el cuadrado y lo asigna
    return new_dict


# Versión con comprensión de diccionarios
squares_comprehensions = {i: i ** 2 for i in range(1, 11)}

# Ejemplo de uso
print(squares_dictionary())
print(squares_comprehensions)