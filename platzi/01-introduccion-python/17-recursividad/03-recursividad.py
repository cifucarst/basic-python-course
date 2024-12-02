# Optimización de la recursividad
# Memoización
# Ejemplo: Fibonacci optimizado

def fibonacci_mem(n, memo={}):
    if n in memo:  # Verificar si el resultado ya está almacenado
        return memo[n]
    if n == 0:  # Caso base
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_mem(n - 1, memo) + fibonacci_mem(n - 2, memo)  # Guardar resultado
    return memo[n]

print(fibonacci_mem(50))  # Salida: 12586269025 (rápido gracias a memoización)



# Recursividad de cola
def factorial_tail(n, acumulador=1):
    if n == 0:  # Caso base
        return acumulador
    return factorial_tail(n - 1, acumulador * n)  # Caso recursivo en cola

print(factorial_tail(5))  # Salida: 120
