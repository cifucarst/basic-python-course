# Ejercicio 4: Números divisibles

# Dado el rango de números entre 1 y 100, genera una lista que contenga solo aquellos números divisibles 
# entre 3 y 5.

divisibles = [i for i in range(1,101) if i % 3 == 0 and i % 5 == 0]
print(divisibles)