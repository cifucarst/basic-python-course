# # Ejercicio 2: Invertir diccionario

# # Escribe una función invertir_diccionario(dic) que tome un diccionario y retorne uno nuevo donde las claves sean los valores del original, y los valores sean listas de claves originales que tenían ese valor.

# # Ejemplo:
salida = {1: ["a", "c"], 2: ["b"]}

entrada = {"a": 1, "b": 2, "c": 3}

def invertir_diccionario(dic):
    """
    Invierte un diccionario. Los valores originales se convierten en claves,
    y las claves originales se agrupan en listas como valores si hay duplicados.
    """
    new_dict = {}
    for key, value in dic.items():
        if value not in new_dict:
            new_dict[value] = []  # Inicializa una lista si el valor no está
        new_dict[value].append(key)  # Agrega la clave a la lista
    return new_dict


# Ejemplo de uso
entrada = {"a": 1, "b": 2, "c": 1}
print(invertir_diccionario(entrada))