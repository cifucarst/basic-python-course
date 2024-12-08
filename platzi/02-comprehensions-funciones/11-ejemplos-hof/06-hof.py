# Ejemplo 6: Ordenar dinámicamente una lista
# Descripción:
# Usar una función de orden superior para ordenar una lista con base en criterios personalizados.


personas = [
    {"nombre": "Andrés", "edad": 25},
    {"nombre": "Juanito", "edad": 30},
    {"nombre": "María", "edad": 20},
]

# Ordenar por nombre
personas_ordenadas_nombre = sorted(personas, key=lambda p: p["nombre"])
print(personas_ordenadas_nombre)
# Salida: [{'nombre': 'Andrés', 'edad': 25}, {'nombre': 'Juanito', 'edad': 30}, {'nombre': 'María', 'edad': 20}]

# Ordenar por edad
personas_ordenadas_edad = sorted(personas, key=lambda p: p["edad"])
print(personas_ordenadas_edad)
# Salida: [{'nombre': 'María', 'edad': 20}, {'nombre': 'Andrés', 'edad': 25}, {'nombre': 'Juanito', 'edad': 30}]