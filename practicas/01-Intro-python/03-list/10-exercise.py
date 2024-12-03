# Ejercicio 10: Lista de números primos

# Crea una función que reciba un número entero n y devuelva una lista con todos los números primos menores que n.

def numeros_primos(n):
    """Calcula los números primos menores que n usando la Criba de Eratóstenes.

    Args:
        n (int): El límite superior para encontrar números primos.

    Returns:
        list: Una lista con todos los números primos menores que n.
    """
    if n <= 2:
        return []  # No hay números primos menores que 2

    es_primo = [True] * n
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, n, i):  # Marca múltiplos de i como no primos
                es_primo[j] = False

    return [x for x in range(n) if es_primo[x]]

# Ejemplo de uso:
limite = 20
resultado = numeros_primos(limite)
print(resultado)  # Salida: [2, 3, 5, 7, 11, 13, 17, 19]