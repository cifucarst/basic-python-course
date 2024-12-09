# Ejercicio 4: Sumar valores comunes

# Dado un diccionario de diccionarios, escribe una función sumar_valores_comunes(dic) que retorne un nuevo diccionario donde las claves sean las mismas pero los valores sean la suma de todos los valores internos.

# Ejemplo:

# entrada = {
#     "x": {"a": 1, "b": 2},
#     "y": {"a": 3, "b": 4},
# }
# salida = {"x": 3, "y": 7}



def sumar_valores_comunes(dic):
    """
    Suma los valores internos de un diccionario de diccionarios.

    Args:
        dic: Un diccionario de diccionarios.

    Returns:
        Un nuevo diccionario con las mismas claves y los valores sumados.
    """
    return {key: sum(value.values()) for key, value in dic.items()}


# Ejemplo de uso
entrada = {
    "x": {"a": 1, "b": 2},
    "y": {"a": 3, "b": 4},
}

print(sumar_valores_comunes(entrada))
