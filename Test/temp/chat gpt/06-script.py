# Nivel Avanzado (Comprensiones, Archivos y Manejo de Errores)

# Comprensiones de listas:
# Dada la lista [1, 2, 3, 4, 5, 6, 7, 8, 9], usa una comprensión de lista para
#  generar una nueva lista con los cuadrados de los números impares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cuadrados_impares = [i**2 for i in lista if i % 2 != 0]

print(cuadrados_impares)


### Mejora ###

# Generar una lista con los cuadrados de los números impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cuadrados_impares = [n**2 for n in numeros if n % 2 != 0]
print("Cuadrados de los impares:", cuadrados_impares)