# Ejemplo 3: Caché con funciones de orden superior
# Descripción:
# Implementar un sistema de caché para optimizar funciones que se llaman repetidamente con los mismos argumentos.


def memoizar(func):
    cache = {}
    def envoltura(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return envoltura

# Función costosa
@memoizar
def calcular_fibonacci(n):
    if n <= 1:
        return n
    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

# Probar con y sin memoización
print(calcular_fibonacci(10))  # Salida: 55
print(calcular_fibonacci(35))  # Mucho más rápido gracias a la caché