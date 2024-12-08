# Ejemplo 4: Generador de funciones de validación
# Descripción:
# Crear un generador de validadores para validar datos dinámicamente.


def crear_validador(comparador, limite):
    return lambda x: comparador(x, limite)

# Crear validadores
es_mayor = crear_validador(lambda x, y: x > y, 18)
es_menor = crear_validador(lambda x, y: x < y, 60)

# Validar edades
edades = [10, 20, 30, 70]
resultados = [es_mayor(edad) and es_menor(edad) for edad in edades]

print(resultados)  # Salida: [False, True, True, False]