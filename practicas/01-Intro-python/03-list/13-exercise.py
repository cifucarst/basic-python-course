# Ejercicio 13: Flatten de una lista anidada

# Dada una lista que contiene listas dentro (como una lista anidada), genera una nueva lista con todos los elementos en un solo nivel.

from typing import Any, List

def aplanar_lista(lista: List[Any]) -> List[Any]:
    """Aplana una lista anidada en una lista unidimensional.

    Args:
        lista (List[Any]): La lista anidada a aplanar.

    Returns:
        List[Any]: Una nueva lista con todos los elementos en un solo nivel.
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)
    return resultado

# Ejemplo de uso:
lista_anidada = [1, [2, 3], 4, [5, 6, [7]]]
lista_aplanada = aplanar_lista(lista_anidada)
print(lista_aplanada)  # Salida: [1, 2, 3, 4, 5, 6, 7]