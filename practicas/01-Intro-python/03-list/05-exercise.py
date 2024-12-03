# Ejercicio 5: Concatenar listas

# Dadas dos listas, combina sus elementos en una sola lista.

def concatenar_listas(*listas):
    """Concatena múltiples listas en una sola.

    Args:
        *listas: Varias listas a concatenar.

    Returns:
        list: Una lista que combina todas las listas proporcionadas.
    """
    resultado = []
    for lista in listas:
        resultado += lista
    return resultado

if __name__ == '__main__':
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [6, 7, 8]
    lista3 = [9, 10]
    print(concatenar_listas(lista1, lista2, lista3))