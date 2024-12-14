# Escribir en archivos CSV
# Puedes escribir datos en un archivo CSV usando csv.writer o csv.DictWriter.

# Ejemplo con csv.writer:


import csv

# Datos a escribir
empleados = [
    ["Nombre", "Edad", "Cargo", "Salario"],
    ["Luis Martínez", 29, "Gerente", 5000],
    ["Ana López", 24, "Diseñadora", 3500]
]

# Escribir archivo CSV
with open('nuevo_empleados.csv', 'w', encoding='utf-8', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(empleados)


##############################################################################

# Ejemplo con csv.DictWriter:

import csv

# Datos a escribir
empleados = [
    {"Nombre": "Luis Martínez", "Edad": 29, "Cargo": "Gerente", "Salario": 5000},
    {"Nombre": "Ana López", "Edad": 24, "Cargo": "Diseñadora", "Salario": 3500},
]

# Escribir archivo CSV como diccionario
with open('nuevo_empleados_dict.csv', 'w', encoding='utf-8', newline='') as archivo:
    campos = ["Nombre", "Edad", "Cargo", "Salario"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(empleados)