# mas ejemplos de listas de diccionarios
# Lista de múltiples productos:

productos = [
    {'nombre': 'jabon', 'precio': 15.0, 'stock': 10},
    {'nombre': 'shampoo', 'precio': 35.0, 'stock': 5},
    {'nombre': 'pasta dental', 'precio': 20.0, 'stock': 8}
]

# Calcular el valor total del inventario:
total_inventario = sum(item['precio'] * item['stock'] for item in productos)
print(f"Valor total del inventario: {total_inventario}")


# Buscar un producto específico:
producto_buscado = 'shampoo'
for producto in productos:
    if producto['nombre'] == producto_buscado:
        print(f"Producto encontrado: {producto}")
        break
else:
    print("Producto no encontrado.")



# ¿Para qué se utiliza?
# Gestión de inventarios: Representar productos con atributos como nombre, precio y cantidad.
# Procesamiento de datos: Manejar datos estructurados provenientes de fuentes como archivos JSON o bases de datos.
# Sistemas de catálogo: Para mostrar información de múltiples elementos en aplicaciones de e-commerce, bibliotecas, etc.
# Esta estructura es flexible, fácil de manipular y una solución común para almacenar datos estructurados en aplicaciones simples.