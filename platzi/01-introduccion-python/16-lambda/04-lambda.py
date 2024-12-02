# Composición de funciones
# Ejemplo: Calcular la longitud de una lista de palabras que cumplen una condición

palabras = ["Python", "lambda", "funciones", "map", "filter"]
condicion = lambda p: len(p) > 5
longitudes = list(map(lambda p: len(p), filter(condicion, palabras)))

print(longitudes)  # Salida: [6, 9]