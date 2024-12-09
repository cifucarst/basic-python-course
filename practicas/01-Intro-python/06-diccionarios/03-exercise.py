# Ejercicio 3: Filtrar por valor

# Escribe una función filtrar_por_valor(dic, n) que tome un diccionario y un número entero n. Retorne un nuevo diccionario que contenga solo las claves y valores donde el valor es mayor que n.

# Ejemplo:

def filtrar_por_valor(dic, n):
    """
    Filtra un diccionario y devuelve uno nuevo con claves y valores
    donde el valor es numérico y mayor que `n`.
    """
    return {key: value for key, value in dic.items() if isinstance(value, (int, float)) and value > n}


# Ejemplo de uso
entrada = {
    "a": 5,
    "b": 1,
    "c": 8,
    "d": '3'  # Valor no numérico
}
n = 4

final_dict = filtrar_por_valor(entrada, n)
print(final_dict)