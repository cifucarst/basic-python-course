# Agregar o actualizar elementos

persona = {"nombre": "Ana"}
persona["edad"] = 30  # Agregar una nueva clave-valor
persona["nombre"] = "Ana María"  # Actualizar un valor
print(persona)  # Salida: {'nombre': 'Ana María', 'edad': 30}



# Eliminar elementos

# Usando del
del persona["edad"]

# Usando pop
profesion = persona.pop("profesión", "No especificada")
print(profesion)  # Salida: No especificada



# Métodos útiles de diccionarios
persona = {"nombre": "Juan", "edad": 20}
print(persona.keys())  # Salida: dict_keys(['nombre', 'edad'])
print(persona.values())  # Salida: dict_values(['Juan', 20])
print(persona.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 20)])
