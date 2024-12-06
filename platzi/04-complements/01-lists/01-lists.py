# lista de diccionarios en Python

super_list = [
    {'nombre': 'jabon', 'precio': 15.0, 'stock': 10}
]

print(super_list[0])  # {'nombre': 'jabon', 'precio': 15.0, 'stock': 10}

print('\n')
# Acceder a valores dentro de un diccionario: Puedes usar las claves del diccionario.
print(super_list[0]['nombre'])  # 'jabon'
print(super_list[0]['precio'])  # 15.0
print(super_list[0]['stock'])   # 10


# Modificar valores: Cambiar el valor de una clave en el diccionario.
super_list[0]['stock'] = 20
print(super_list[0]['stock'])  # 20

# Agregar nuevos productos (más diccionarios a la lista):
super_list.append({'nombre': 'shampoo', 'precio': 35.0, 'stock': 5})
print(super_list)

# Iterar sobre la lista: Usar bucles para procesar cada diccionario.
for producto in super_list:
    print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")