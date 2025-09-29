# Diccionarios:
#     Crea un diccionario que contenga el nombre, la edad y la ciudad de una persona.
#     Agrega una nueva clave profesion al diccionario.
#     Recorre el diccionario e imprime cada clave y su valor.

persona = {
    "nombre": "Maya Florez",
    "edad": 32,
    "ciudad": "Medellin"
}

persona['profesion'] = 'Hacker'

for key, value in persona.items():
    print(f'{key} - {value}')



### Mejora ###


persona = {
    "nombre": "Maya Florez",
    "edad": 32,
    "ciudad": "Medellín"
}

# Agregar nueva clave
persona['profesion'] = 'Hacker'

print("Datos de la persona:")
for key, value in persona.items():
    print(f"{key.capitalize()} - {value}")
