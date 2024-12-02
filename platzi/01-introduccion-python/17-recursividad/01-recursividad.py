# sintaxis basica

def funcion_recursiva(parametro):
    if caso_base:  # Detener la recursión
        return resultado
    else:
        return funcion_recursiva(nuevo_parametro)



# Ejemplos básicos
# Factorial de un número

def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    return n * factorial(n - 1)  # Caso recursivo

print(factorial(5))  # Salida: 120



# Serie de Fibonacci
def fibonacci(n):
    if n == 0:  # Caso base
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

print(fibonacci(6))  # Salida: 8
