# Ejercicio 7: Desglose de palabras

# Dada una frase como:
frase = "Aprender Python es muy divertido"

# Crea una lista que contenga el número de letras de cada palabra.

frase = "Aprender Python es muy divertido"
numero_letras = [len(palabra) for palabra in frase.split()]
print(numero_letras)

#/////////////////////////////////////////////////////////////////////////


# Alternativa: Excluir signos de puntuación

# Si la frase puede contener puntuación, puedes eliminarla con una comprensión adicional o usando expresiones regulares:

import re

# Genera una lista con el número de letras de cada palabra excluyendo puntuación
numero_letras = [len(re.sub(r'[^a-zA-Z]', '', palabra)) for palabra in frase.split()]
print(numero_letras)
