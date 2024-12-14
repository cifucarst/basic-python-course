# Leer y analizar un archivo de configuración
# Supongamos que tienes un archivo .txt con una estructura de configuración:

# Archivo: config.txt

    # host=127.0.0.1
    # port=8080
    # debug=True


# Código para leer y convertirlo en un diccionario:

def leer_configuracion(archivo):
    configuracion = {}
    with open(archivo, "r") as f:
        for linea in f:
            if "=" in linea:
                clave, valor = linea.strip().split("=", 1)
                configuracion[clave] = valor
    return configuracion

config = leer_configuracion("config.txt")
print(config)


# Salida:
# {'host': '127.0.0.1', 'port': '8080', 'debug': 'True'}