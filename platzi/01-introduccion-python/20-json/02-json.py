# Deserializar datos JSON a Python

import json

# JSON como cadena
datos_json = '''
{
    "nombre": "Andrés",
    "edad": 25,
    "ciudad": "Bogotá",
    "habilidades": ["Python", "JavaScript", "C++"]
}
'''

# Convertir JSON a un diccionario de Python
datos_python = json.loads(datos_json)
print(datos_python)
print(datos_python["habilidades"])  # Salida: ['Python', 'JavaScript', 'C++']




# Trabajar con archivos JSON
# Guardar datos en un archivo JSON
import json

# Datos en Python
datos = {
    "producto": "Laptop",
    "precio": 750,
    "disponible": True
}

# Escribir datos en un archivo
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)



# Leer datos desde un archivo JSON
import json

# Leer datos desde el archivo
with open("datos.json", "r") as archivo:
    datos_leidos = json.load(archivo)

print(datos_leidos)  # Salida: {'producto': 'Laptop', 'precio': 750, 'disponible': True}
