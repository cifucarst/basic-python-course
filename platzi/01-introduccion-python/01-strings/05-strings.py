# Ejercicios practicos

# palindromos
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

print(es_palindromo("anita lava la tina"))  # True


# contador de vocales
def contar_vocales(texto):
    texto = texto.lower()
    vocales = "aeiou"
    return sum(1 for letra in texto if letra in vocales)

print(contar_vocales("Aprendiendo Python"))  # 7