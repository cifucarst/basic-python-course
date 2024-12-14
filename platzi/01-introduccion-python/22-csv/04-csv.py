# Manipulación avanzada
# Puedes combinar el módulo csv con bibliotecas como pandas para análisis y manipulación más complejos.

# Ejemplo con pandas:


import pandas as pd

# Leer archivo CSV
df = pd.read_csv('empleados.csv')
print(df)

# Filtrar empleados con salario mayor a 4000
empleados_altos_salarios = df[df['Salario'] > 4000]
print(empleados_altos_salarios)

# Guardar el resultado en un nuevo archivo CSV
empleados_altos_salarios.to_csv('empleados_filtrados.csv', index=False)


#################################################################################


# Buenas prácticas

# Usa el parámetro newline='': Al abrir un archivo CSV en modo escritura, esto evita líneas en blanco inesperadas.
# Especifica la codificación: Usa utf-8 para manejar caracteres especiales como tildes.
# Manejo de excepciones: Siempre maneja posibles errores como archivos inexistentes o problemas de formato.
# Ejemplo con manejo de errores:



import csv

try:
    with open('empleados.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
except FileNotFoundError:
    print("El archivo no fue encontrado.")
except csv.Error as e:
    print(f"Error al procesar el archivo CSV: {e}")