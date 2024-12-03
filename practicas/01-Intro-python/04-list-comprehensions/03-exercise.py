# Ejercicio 3: Cuadrados de impares

# Usa una comprensión de lista para crear una lista que contenga los cuadrados de los números impares del 1 al 20.

squares_odd = [i**2 for i in range(1, 20, 2)]
print(squares_odd)