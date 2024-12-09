# El módulo collections en Python proporciona clases y estructuras de datos especializadas que extienden las capacidades de las colecciones estándar como listas, tuplas y diccionarios. Estas herramientas son útiles para manejar datos de forma más eficiente y legible.

# 1. Counter
# Es una subclase de diccionario diseñada para contar elementos hashables (como cadenas, números o tuplas).

# Ejemplo: Contar elementos en una lista

from collections import Counter

frutas = ['manzana', 'pera', 'naranja', 'manzana', 'pera', 'manzana']
contador = Counter(frutas)

print(contador)  # Salida: Counter({'manzana': 3, 'pera': 2, 'naranja': 1})

# Métodos útiles
print(contador.most_common(1))  # Elemento más común: [('manzana', 3)]
print(list(contador.elements()))  # Elementos repetidos: ['manzana', 'manzana', 'manzana', 'pera', 'pera', 'naranja']