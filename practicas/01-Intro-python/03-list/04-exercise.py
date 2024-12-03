# Ejercicio 4: Índices de un elemento

# Escribe un programa que encuentre todos los índices de un elemento específico en una lista. Si el elemento no está presente, imprime un mensaje adecuado.

def encontrar_indices(lista, elemento):
    """Encuentra todos los índices de un elemento en una lista.

    Args:
        lista (list): La lista en la que buscar el elemento.
        elemento (any): El elemento a buscar.

    Returns:
        list: Una lista con los índices donde se encuentra el elemento, o una lista vacía si no se encuentra.
    """
    return [i for i, x in enumerate(lista) if x == elemento]

# Ejemplo de uso:
mi_lista = [1, 2, 3, 2, 4, 2]
elemento_a_buscar = 2

resultado = encontrar_indices(mi_lista, elemento_a_buscar)
if resultado:
    print(f"El elemento '{elemento_a_buscar}' se encuentra en los índices: {resultado}")
else:
    print(f"El elemento '{elemento_a_buscar}' no se encuentra en la lista.")