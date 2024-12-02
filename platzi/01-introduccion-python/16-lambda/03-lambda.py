# Ejemplos avanzados
# Condicionales dentro de una lambda

# Ejemplo: Verificar si un número es par o impar

par_impar = lambda x: "Par" if x % 2 == 0 else "Impar"
print(par_impar(5))  # Salida: Impar
print(par_impar(8))  # Salida: Par



# Lambdas con múltiples argumentos
# Ejemplo: Calcular el área de un triángulo
area_triangulo = lambda base, altura: (base * altura) / 2
print(area_triangulo(10, 5))  # Salida: 25.0



# Usar lambdas en diccionarios
# Ejemplo: Crear un menú de operaciones matemáticas

operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
    "multiplicación": lambda x, y: x * y,
    "división": lambda x, y: x / y if y != 0 else "Indefinido"
}

print(operaciones["suma"](10, 5))             # Salida: 15
print(operaciones["división"](10, 0))        # Salida: Indefinido



# Lambdas con listas de comprensión
# Ejemplo: Aplicar una operación condicional a una lista

numeros = [1, 2, 3, 4, 5]
resultado = [(lambda x: x**2 if x % 2 == 0 else x**3)(n) for n in numeros]
print(resultado)  # Salida: [1, 4, 27, 16, 125]