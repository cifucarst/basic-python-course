# Aplicar operaciones complejas

# Calcular factorial de números en un rango
import math

factoriales = {x: math.factorial(x) for x in range(1, 6)}
print(factoriales)  
# Salida: {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}



# Agrupar elementos por condición
# Clasificar números en "menores" y "mayores"
numeros = [1, 8, 3, 12, 5]
clasificacion = {"menores": [x for x in numeros if x < 10], 
                 "mayores": [x for x in numeros if x >= 10]}

print(clasificacion)
# Salida: {'menores': [1, 8, 3, 5], 'mayores': [12]}