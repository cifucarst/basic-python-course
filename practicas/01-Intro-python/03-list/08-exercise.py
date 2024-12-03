# Ejercicio 8: Sublistas de tamaño fijo

# Dada una lista y un número entero n, divide la lista en sublistas de tamaño n. Si no es posible dividirla exactamente, la última sublista puede tener menos elementos.


def dividir_lista(lista, n):
    """Divide una lista en sublistas de tamaño n.

    Args:
        lista (list): La lista a dividir.
        n (int): El tamaño deseado de cada sublista.

    Returns:
        list: Una lista de sublistas. Si `n <= 0`, devuelve una lista vacía.
    """
    if n <= 0:  # Manejo de tamaños de sublista inválidos
        return []
    return [lista[i:i + n] for i in range(0, len(lista), n)]

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tamaño_sublista = 3

resultado = dividir_lista(mi_lista, tamaño_sublista)
print(resultado)  # Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]