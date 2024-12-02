# Crear un diccionario vacío
diccionario_vacio = {}

# Crear un diccionario con datos
persona = {
    "nombre": "Andrés",
    "edad": 25,
    "ciudad": "Bogotá"
}

# Acceder a un valor
print(persona["nombre"])  # Salida: Andrés



# Métodos importantes de los diccionarios
# Acceso a los valores
persona = {"nombre": "Ana", "edad": 30, "profesión": "Ingeniera"}
print(persona["edad"])  # Salida: 30

# Si intentas acceder a una clave inexistente, obtendrás un error:
print(persona["altura"])  # KeyError

# Para evitarlo, usa el método get():
print(persona.get("altura", "No disponible"))  # Salida: No disponible