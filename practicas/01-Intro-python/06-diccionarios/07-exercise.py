# Ejercicio 3: Invertir claves y valores

# Dado un diccionario:

# entrada = {"a": 1, "b": 2, "c": 3}

# Usa comprensión de diccionarios para crear un nuevo diccionario donde los valores se conviertan en claves y las claves en valores.

# Ejemplo esperado:

# {1: "a", 2: "b", 3: "c"}



entrada = {"a": 1, "b": 2, "c": 3}

# Intercambiar claves y valores en el diccionario
result = {value: key for key, value in entrada.items()}

print(result)