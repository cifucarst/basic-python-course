# Ejercicio 7: Rotación de elementos

# Crea una función que reciba una lista y un número n y devuelva una nueva lista con los
#  elementos rotados hacia la derecha n posiciones.

def rotar_derecha(lista, n):
    """Rota los elementos de una lista hacia la derecha n posiciones.

    Args:
        lista (list): La lista de elementos a rotar.
        n (int): El número de posiciones a rotar hacia la derecha.

    Returns:
        list: Una nueva lista con los elementos rotados, o la lista original si está vacía.
    """
    if not lista:  # Manejo de lista vacía
        return lista
    n = n % len(lista)  # Asegurar que n esté dentro del rango de la lista
    if n == 0:  # Si no se necesita rotación
        return lista
    return lista[-n:] + lista[:-n]

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
posiciones_a_rotar = 2

nueva_lista = rotar_derecha(mi_lista, posiciones_a_rotar)
print(nueva_lista)  # Salida: [4, 5, 1, 2, 3]