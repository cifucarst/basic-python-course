# Extraer columnas específicas de un archivo tabular
# Supongamos que tienes un archivo data.txt con datos tabulares separados por comas:

# Archivo: data.txt


# nombre,edad,ciudad
# Andrés,25,Bogotá
# Juan,30,Medellín
# María,28,Cali

# Código para extraer nombres y ciudades:


def extraer_columnas(archivo, columnas):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    encabezados = lineas[0].strip().split(",")
    indices = [encabezados.index(col) for col in columnas]
    datos = []
    for linea in lineas[1:]:
        valores = linea.strip().split(",")
        datos.append([valores[i] for i in indices])
    return datos

columnas_deseadas = ["nombre", "ciudad"]
resultado = extraer_columnas("data.txt", columnas_deseadas)
print(resultado)



# Salida:

# [['Andrés', 'Bogotá'], ['Juan', 'Medellín'], ['María', 'Cali']]