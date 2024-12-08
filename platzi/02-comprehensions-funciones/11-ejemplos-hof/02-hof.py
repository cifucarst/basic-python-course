# Ejemplo 2: Generador de saludos personalizados
# Descripción:
# Una función que devuelve otra función para personalizar saludos.

def generar_saludo(saludo):
    def saludar(nombre):
        return f"{saludo}, {nombre}!"
    return saludar

# Crear saludos personalizados
saludo_espanol = generar_saludo("Hola")
saludo_ingles = generar_saludo("Hello")

print(saludo_espanol("Andrés"))  # Salida: Hola, Andrés!
print(saludo_ingles("Juanito")) # Salida: Hello, Juanito!