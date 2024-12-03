# Ejercicio 12: Comparar dos listas

# Escribe un programa que reciba dos listas y genere una nueva lista con los elementos que están en ambas listas (intersección).

def interseccion_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    """Encuentra los elementos comunes entre dos listas.

    Args:
        lista1 (list[int]): La primera lista.
        lista2 (list[int]): La segunda lista.

    Returns:
        list[int]: Una nueva lista con los elementos que están en ambas listas, en el orden de lista1.
    """
    conjunto2 = set(lista2)
    return [elemento for elemento in lista1 if elemento in conjunto2]

# Ejemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

resultado = interseccion_listas(lista1, lista2)
print(resultado)  # Salida: [3, 4, 5]