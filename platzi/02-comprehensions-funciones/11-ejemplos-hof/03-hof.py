# Ejemplo 3: Uso de map, filter y reduce combinados
# Descripción:
# Procesar una lista de productos con precios, calcular impuestos y sumar los totales.


from functools import reduce

productos = [
    {"nombre": "Producto 1", "precio": 100},
    {"nombre": "Producto 2", "precio": 200},
    {"nombre": "Producto 3", "precio": 150},
]

# Paso 1: Extraer los precios y calcular con impuesto (20%)
precios_con_impuesto = map(lambda p: p["precio"] * 1.2, productos)

# Paso 2: Filtrar precios mayores a 150
precios_filtrados = filter(lambda precio: precio > 150, precios_con_impuesto)

# Paso 3: Sumar los precios restantes
total = reduce(lambda x, y: x + y, precios_filtrados)

print(total)  # Salida: 420.0