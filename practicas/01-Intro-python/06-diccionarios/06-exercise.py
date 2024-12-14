# Ejercicio 2: Filtrar un diccionario

# Dado el siguiente diccionario:

# entrada = {"a": 5, "b": 3, "c": 8, "d": 1, "e": 9}

# Usa comprensión de diccionarios para crear uno nuevo que contenga solo las claves y valores donde el valor sea mayor que 5.

# Ejemplo esperado:

# {"c": 8, "e": 9}


entrada = {"a": 5, "b": 3, "c": 8, "d": 1, "e": 9}

# Filtrar claves y valores donde el valor es mayor que 5
result = {key: value for key, value in entrada.items() if value > 5}

print(result)