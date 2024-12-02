# Trabajar con cadenas
# Extraer vocales de una cadena

cadena = "programación"
vocales = [letra for letra in cadena if letra in 'aeiou']
print(vocales)  # ['o', 'a', 'a', 'i', 'ó']


# Crear una lista de palabras largas
oracion = "Python es un lenguaje de programación poderoso"
largas = [palabra for palabra in oracion.split() if len(palabra) > 5]
print(largas)  # ['lenguaje', 'programación', 'poderoso']