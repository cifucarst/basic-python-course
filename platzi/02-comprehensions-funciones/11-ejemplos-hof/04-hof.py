# Ejemplo 4: Decoradores
# Descripción:
# Un decorador es una función de orden superior que modifica el comportamiento de otra función.


def decorador_mayusculas(func):
    def envoltura(texto):
        resultado = func(texto)
        return resultado.upper()
    return envoltura

# Función base
@decorador_mayusculas
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Andrés"))  # Salida: HOLA, ANDRÉS