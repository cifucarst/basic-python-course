# Ejemplos de strings
cadena_simple = 'Hola, Python'
cadena_doble = "Hola, Mundo"
cadena_multilinea = """Este es
un texto
en varias líneas."""


# Propiedades de los strings
texto = "Hola"
# Esto genera un nuevo string; no modifica el original
nuevo_texto = texto + ", ¿cómo estás?"
# print(texto)         # Hola
# print(nuevo_texto)   # Hola, ¿cómo estás?


# indexacion
texto = "Python"
print(texto[0])  # P
print(texto[-1]) # n


# slicing
texto = "Aprendiendo Python"
print(texto[0:10])    # Aprendiendo
print(texto[:10])     # Aprendiendo (inicio implícito 0)
print(texto[11:])     # Python (fin implícito)
print(texto[::2])     # ApededoPto (salta de dos en dos)


# operaciones comunes

# concatenacion
saludo = "Hola, "
nombre = "Andrés"
print(saludo + nombre)  # Hola, Andrés


# repeticion
print("Python! " * 3)  # Python! Python! Python!

# longitud
frase = "Aprender Python es divertido"
print(len(frase))  # 28