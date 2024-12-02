# Metodos de string
texto = "hOlA, PYTHON"
print(texto.lower())      # hola, python
print(texto.upper())      # HOLA, PYTHON
print(texto.capitalize()) # Hola, python
print(texto.title())      # Hola, Python


# Espacios
texto = "   Hola, Mundo   "
print(texto.strip())  # "Hola, Mundo"
print(texto.lstrip()) # "Hola, Mundo   "
print(texto.rstrip()) # "   Hola, Mundo"


# Busqueda y reemplazo
texto = "Me encanta Python"
print(texto.find("Python"))  # 10
print(texto.replace("Python", "programar"))  # Me encanta programar


# Division y union
texto = "uno, dos, tres"
lista = texto.split(", ")
print(lista)  # ['uno', 'dos', 'tres']

texto_unido = " - ".join(lista)
print(texto_unido)  # uno - dos - tres