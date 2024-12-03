# Ejercicio 3: Eliminar duplicados

# Dada una lista con elementos duplicados, genera una nueva lista sin duplicados, manteniendo el orden de aparición.


def eliminar_duplicados(lista):
    return list(set(lista))


if __name__ == '__main__':
    lista = [1,2,3,4,5,1,3,4,5,1,1]
    print(eliminar_duplicados(lista))


# //////////////////////////////////////////////////////////////////////////////////

# Mejora Opcional: Mantener el orden

# Si quieres eliminar duplicados y conservar el orden de los elementos, puedes usar una 
# comprensión de listas junto con un conjunto para rastrear los elementos ya vistos:

def eliminar_duplicados(lista):
    vistos = set()
    return [x for x in lista if x not in vistos and not vistos.add(x)]

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 1, 3, 4, 5, 1, 1]
    print(eliminar_duplicados(lista))