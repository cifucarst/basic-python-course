# Buscar y reemplazar texto en un archivo
# Este código reemplaza todas las ocurrencias de una palabra en un archivo.

# Código:


def buscar_y_reemplazar(archivo, buscar, reemplazar):
    with open(archivo, "r") as f:
        contenido = f.read()
    contenido_modificado = contenido.replace(buscar, reemplazar)
    with open(archivo, "w") as f:
        f.write(contenido_modificado)

buscar_y_reemplazar("archivo.txt", "Python", "Dart")
print("Texto reemplazado con éxito.")