# Generar un índice invertido desde un archivo
# Crea un índice de palabras indicando en qué líneas aparecen.

# Código:


from collections import defaultdict

def crear_indice_invertido(archivo):
    indice = defaultdict(list)
    with open(archivo, "r") as f:
        for num_linea, linea in enumerate(f, start=1):
            for palabra in linea.strip().split():
                indice[palabra].append(num_linea)
    return dict(indice)

indice = crear_indice_invertido("archivo.txt")
print(indice)


# Salida (ejemplo):

# {'Python': [1, 3], 'es': [1], 'genial': [1], 'Dart': [2]}