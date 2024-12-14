# Procesar un archivo de log
# Un archivo logs.txt contiene datos como este:


# [INFO] 2024-12-12 10:00:00 - User login
# [ERROR] 2024-12-12 10:01:00 - Connection failed
# [INFO] 2024-12-12 10:05:00 - File uploaded

# Código para filtrar solo los errores:


def filtrar_errores(archivo):
    with open(archivo, "r") as f:
        errores = [linea for linea in f if "[ERROR]" in linea]
    return errores

errores = filtrar_errores("logs.txt")
for error in errores:
    print(error.strip())