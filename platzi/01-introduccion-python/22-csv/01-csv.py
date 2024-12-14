# ¿Qué es un archivo CSV?
# CSV (Comma-Separated Values) es un formato de archivo donde los datos están separados por comas (aunque también pueden usarse otros delimitadores como ; o tabulaciones). Este formato es ampliamente usado para almacenar datos tabulares, como los de una hoja de cálculo.

# Ejemplo de un archivo empleados.csv:

# Nombre,Edad,Cargo,Salario
# Andrés Pérez,25,Ingeniero de Software,4500
# Juanito Ramírez,30,Analista de Sistemas,4000
# María Gómez,27,Desarrolladora Web,4200


# Trabajar con CSV en Python
# Python proporciona el módulo csv para trabajar con estos archivos de manera sencilla y eficiente.

# 1. Leer archivos CSV
# Para leer un archivo CSV, puedes usar el método csv.reader o csv.DictReader.

# Ejemplo con csv.reader:

import csv

# Leer archivo CSV
with open('empleados.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)


# Salida

# ['Nombre', 'Edad', 'Cargo', 'Salario']
# ['Andrés Pérez', '25', 'Ingeniero de Software', '4500']
# ['Juanito Ramírez', '30', 'Analista de Sistemas', '4000']
# ['María Gómez', '27', 'Desarrolladora Web', '4200']