# operaciones avanzadas

# corto circuito

# Cortocircuito con and
print(False and print("No se evalúa esto"))

# Cortocircuito con or
print(True or print("No se evalúa esto"))


# booleanos en colecciones
# Uso como índice
valores = ["falso", "verdadero"]
print(valores[True])  # "verdadero"
print(valores[False]) # "falso"

# Uso como clave en diccionarios
estado = {True: "Encendido", False: "Apagado"}
print(estado[True])   # "Encendido"