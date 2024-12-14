# Ejercicio 7: Contar letras en una frase

# Dada una frase:

# frase = "hola mundo"

# Usa comprensión de diccionarios para contar cuántas veces aparece cada letra en la frase, ignorando los espacios.

# Ejemplo esperado:

# {"h": 1, "o": 2, "l": 1, "a": 1, "m": 1, "u": 1, "n": 1, "d": 1}

from collections import Counter

frase = "hola mundo"

# Contar la frecuencia de cada carácter, ignorando espacios
result = dict(Counter(frase.replace(" ", "")))

print(result)