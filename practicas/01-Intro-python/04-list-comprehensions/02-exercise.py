# Ejercicio 2: Palabras largas

# Dada la lista palabras = ["python", "comprehension", "código", "práctica", "listas"], genera una nueva lista que contenga solo las palabras con más de 7 caracteres.

words = ["python", "comprehension", "código", "práctica", "listas"]
long_words = [word for word in words if len(word) > 7]
print(long_words)