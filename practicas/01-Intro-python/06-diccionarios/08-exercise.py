# Ejercicio 4: Multiplicar valores

# Dado un diccionario:

# entrada = {"x": 10, "y": 20, "z": 30}

# Usa comprensión de diccionarios para crear uno nuevo donde los valores sean el doble de los originales.

# Ejemplo esperado:

# {"x": 20, "y": 40, "z": 60}


entrada = {"x": 10, "y": 20, "z": 30}

# Crear un nuevo diccionario donde los valores sean el doble de los originales
result = {key: value * 2 for key, value in entrada.items()}

print(result)