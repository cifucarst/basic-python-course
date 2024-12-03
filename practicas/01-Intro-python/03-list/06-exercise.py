# Ejercicio 6: Promedio de una lista

# Calcula el promedio de los números en una lista.

def calcular_promedio(lista):
    if not lista:  # Verifica si la lista está vacía
        return "La lista está vacía, no se puede calcular el promedio."
    return sum(lista) / len(lista)

def run():
    lista = [1, 2, 3, 4, 5, 6]
    promedio = calcular_promedio(lista)
    print(f'El promedio de la lista introducida es: {promedio}')

if __name__ == '__main__':
    run()



# ////////////////////////////////////////////////////////////////////////////

# Otra opcion con try-except

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def run():
    lista = []
    try:
        promedio = calcular_promedio(lista)
        print(f'El promedio de la lista introducida es: {promedio}')
    except ZeroDivisionError:
        print("La lista está vacía, no se puede calcular el promedio.")

if __name__ == '__main__':
    run()