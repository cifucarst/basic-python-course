# Ejemplo avanzado: Lectura de archivos

try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
except IOError:
    print("Error al leer el archivo.")
finally:
    print("Operación de archivo finalizada.")