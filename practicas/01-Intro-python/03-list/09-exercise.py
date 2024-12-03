# Ejercicio 9: Producto de pares

# Dada una lista de números, genera una nueva lista que contenga el producto de cada par de números consecutivos.

def producto_pares(lista):
    """Calcula el producto de pares consecutivos en una lista.

    Args:
        lista (list): La lista de números.

    Returns:
        list: Una nueva lista con los productos de los pares consecutivos.
    """
    return [lista[i] * lista[i + 1] for i in range(len(lista) - 1)]

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
resultado = producto_pares(mi_lista)
print(resultado)  # Salida: [2, 6, 12, 20]