# Ejemplos mas avanzados

# Ejemplos avanzados
# Generador infinito
def contador_infinito(inicio=0):
    while True:
        yield inicio
        inicio += 1

contador = contador_infinito()

for _ in range(5):
    print(next(contador))
# Salida:
# 0
# 1
# 2
# 3
# 4



# Generador para leer grandes archivos línea a línea
def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()

# Uso
for linea in leer_lineas('archivo.txt'):
    print(linea)


