# Ejercicio 11: Eliminar elementos según condición

# Dada una lista de números, elimina todos los elementos que sean divisibles por un número x proporcionado por el usuario.

def eliminar_divisibles(lista: list[int], divisor: int) -> list[int]:
    """Elimina los elementos de una lista que son divisibles por un divisor.

    Args:
        lista (list[int]): La lista de números.
        divisor (int): El número por el cual se verificará la divisibilidad.

    Returns:
        list[int]: Una nueva lista sin los elementos divisibles.
    """
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    return [num for num in lista if num % divisor != 0]

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
divisor = 3

resultado = eliminar_divisibles(mi_lista, divisor)
print(resultado)  # Salida: [1, 2, 4, 5, 7, 8]