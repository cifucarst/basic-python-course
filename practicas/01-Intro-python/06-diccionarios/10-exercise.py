# Ejercicio 6: Filtrar valores numéricos

# Dado un diccionario que contiene valores mixtos:

# entrada = {"a": 10, "b": "hello", "c": 15, "d": [1, 2, 3], "e": 20}

# Usa comprensión de diccionarios para crear uno nuevo que contenga solo los pares clave-valor donde el valor sea numérico.

# Ejemplo esperado:

# {"a": 10, "c": 15, "e": 20}


entrada = {"a": 10, "b": "hello", "c": 15, "d": [1, 2, 3], "e": 20}

# Filtrar claves y valores donde el valor sea de tipo entero
result = {key: value for key, value in entrada.items() if isinstance(value, int)}
print(result)