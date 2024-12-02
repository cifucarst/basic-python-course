# Ejemplos prácticos
# Contar palabras en un texto

texto = "python es genial y python es fácil"
contador = {}

for palabra in texto.split():
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)  # Salida: {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'fácil': 1}



# Convertir listas en un diccionario
claves = ["nombre", "edad", "profesión"]
valores = ["Luisa", 28, "Diseñadora"]

diccionario = dict(zip(claves, valores))
print(diccionario)  # Salida: {'nombre': 'Luisa', 'edad': 28, 'profesión': 'Diseñadora'}



# Iterar sobre un diccionario
persona = {"nombre": "Carlos", "edad": 35, "ciudad": "Medellín"}

# Iterar sobre claves
for clave in persona:
    print(clave)

# Iterar sobre valores
for valor in persona.values():
    print(valor)

# Iterar sobre claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")



# Diccionarios anidados
empresa = {
    "departamento_ventas": {"empleados": 10, "ingresos": 50000},
    "departamento_ti": {"empleados": 5, "ingresos": 20000}
}

print(empresa["departamento_ventas"]["empleados"])  # Salida: 10