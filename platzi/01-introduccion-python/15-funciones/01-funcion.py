# funcion basica
def nombre_de_la_funcion(parametros):
    """
    Documentación opcional sobre la función.
    """
    # Código a ejecutar
    return resultado  # Devuelve un valor (opcional)



# Ejemplo básico: Suma de dos números
def sumar(a, b):
    return a + b

# Llamar a la función
resultado = sumar(3, 5)
print(resultado)  # Salida: 8



# Ejemplo: Parámetros posicionales y nombrados
def describir_persona(nombre, edad):
    return f"{nombre} tiene {edad} años."

# Parámetros posicionales
print(describir_persona("Andrés", 25))  # Salida: Andrés tiene 25 años.

# Parámetros nombrados
print(describir_persona(edad=30, nombre="Luis"))  # Salida: Luis tiene 30 años.



# Parámetros por defecto
def saludar(nombre="amigo"):
    return f"Hola, {nombre}!"

print(saludar())           # Salida: Hola, amigo!
print(saludar("Andrés"))   # Salida: Hola, Andrés!