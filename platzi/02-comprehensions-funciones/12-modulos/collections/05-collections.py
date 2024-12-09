# 5. OrderedDict
# Es un diccionario que recuerda el orden en que se agregaron los elementos. Desde Python 3.7, los diccionarios normales también mantienen el orden, pero OrderedDict tiene métodos adicionales.

# Ejemplo: Comparar orden de inserción

from collections import OrderedDict

ordenado = OrderedDict()
ordenado["uno"] = 1
ordenado["dos"] = 2
ordenado["tres"] = 3

print(ordenado)  # Salida: OrderedDict([('uno', 1), ('dos', 2), ('tres', 3)])