# Verificación de tipos

def concatenar_cadenas(cadena1, cadena2):
    assert isinstance(cadena1, str), "El primer argumento debe ser una cadena"
    assert isinstance(cadena2, str), "El segundo argumento debe ser una cadena"
    return cadena1 + cadena2

# Prueba
print(concatenar_cadenas("Hola, ", "mundo"))  # Salida: Hola, mundo
print(concatenar_cadenas("Hola", 5))         # AssertionError: El segundo argumento debe ser una cadena