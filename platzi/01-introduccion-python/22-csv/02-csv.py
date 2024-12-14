# Ejemplo con csv.DictReader:
# DictReader convierte cada fila en un diccionario donde las claves son los encabezados.


import csv

# Leer archivo CSV como diccionario
with open('empleados.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"{fila['Nombre']} - {fila['Cargo']} - ${fila['Salario']}")


# Salida:

# Andrés Pérez - Ingeniero de Software - $4500
# Juanito Ramírez - Analista de Sistemas - $4000
# María Gómez - Desarrolladora Web - $4200