# Archivos y manejo de errores:
#     Escribe un programa que abra un archivo llamado datos.txt, lea su contenido y lo imprima.
#     Si el archivo no existe, captura la excepción y muestra el mensaje “Archivo no encontrado”.



try:
    with open("datos.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError as e:
    print(f"Archivo no encontrado: \n{e}")


### Mejora ###


try:
    with open("datos.txt", "r") as file:
        for line in file:
            print(line.strip())  # Elimina saltos de línea extra
except FileNotFoundError:
    print("Archivo no encontrado. Por favor, verifica el nombre o la ubicación.")