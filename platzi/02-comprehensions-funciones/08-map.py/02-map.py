numbers = [1,2,3,4,5]
numbers_v2 = [5,6,7]

result = list(map(lambda x, y: x + y,numbers, numbers_v2))

# print(result)

# ////////////////////////////////////////////////////////////

# Funciones Integradas de Orden Superior
# map: Aplica una función a cada elemento de un iterable y devuelve un objeto map.

palabras = ["hola", "mundo", "python"]
longitudes = map(len, palabras)
print(list(longitudes))  # Salida: [4, 5, 6]