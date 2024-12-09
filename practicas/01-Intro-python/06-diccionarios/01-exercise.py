# Ejercicio 1: Contar ocurrencias

# Escribe una función contar_ocurrencias(lista) que tome una lista de elementos y retorne un diccionario donde las claves sean los elementos de la lista, y los valores sean la cantidad de veces que cada elemento aparece.

# Ejemplo:
# salida = {"manzana": 3, "pera": 2, "uva": 1}

from collections import Counter

def contar_ocurrencias(lista):
    """
    Retorna un diccionario con la cantidad de ocurrencias de cada elemento en la lista.
    """
    return dict(Counter(lista))  # Convertimos el Counter a un diccionario si se requiere estrictamente.

# Ejemplo de uso
entrada = ["manzana", "pera", "manzana", "pera", "manzana", "uva"]
print(contar_ocurrencias(entrada))