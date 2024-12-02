# Ventajas de las tuplas
# Inmutabilidad: Útil para proteger datos contra cambios accidentales.
# Rendimiento: Las tuplas son más rápidas que las listas debido a su inmutabilidad.
# Usabilidad: Pueden ser utilizadas como claves en diccionarios o almacenadas en estructuras que requieren elementos inmutables.

# Ejemplo práctico completo
# Almacenar coordenadas en un sistema de puntos

puntos = ((0, 0), (1, 2), (3, 4), (-1, -2))

for punto in puntos:
    x, y = punto
    print(f"Coordenada: x={x}, y={y}")



# Emparejar listas usando zip
nombres = ("Ana", "Luis", "Pedro")
edades = (25, 30, 35)

# Crear una lista de tuplas
emparejados = list(zip(nombres, edades))
print(emparejados)  # [('Ana', 25), ('Luis', 30), ('Pedro', 35)]
