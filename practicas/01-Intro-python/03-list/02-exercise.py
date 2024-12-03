# Ejercicio 2: Lista inversa

# Dada una lista, crea una nueva lista con los elementos en orden inverso. No uses el método reverse().

def invertir_lista(lista):
    return lista[::-1]


if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(invertir_lista(lista))


# //////////////////////////////////////////////////////////////////////////////////

# Otro metodo de hacerlo

def invertir_lista(lista):
    return list(reversed(lista))

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(invertir_lista(lista))


# //////////////////////////////////////////////////////////////////////////////////

# otro metodo

def invertir_lista(lista):
    invertida = []
    for elemento in lista:
        invertida.insert(0, elemento)  # Inserta cada elemento al inicio
    return invertida

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(invertir_lista(lista))