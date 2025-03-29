# Ejercicio 1: Validador de Contraseñas Seguras
# Escribe una función en Python llamada validar_contraseña(contraseña) que verifique si una contraseña es segura según los siguientes criterios:

# ✅ Al menos 8 caracteres de longitud
# ✅ Contiene al menos una letra mayúscula
# ✅ Contiene al menos una letra minúscula
# ✅ Contiene al menos un número
# ✅ Contiene al menos un carácter especial (por ejemplo, @, #, $, %, &, *)

# La función debe devolver True si la contraseña es segura y False en caso contrario.

# Ejemplo de uso:

# print(validar_contraseña("HolaMundo123@"))  # Debe devolver True
# print(validar_contraseña("holamundo"))  # Debe devolver False

import string

def validar_contraseña(password: str) -> bool:
    # Verifica que tenga al menos 8 caracteres
    if len(password) < 8:
        return False

    # Verifica que contenga al menos una mayúscula, una minúscula, un número y un carácter especial
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_minuscula = any(c.islower() for c in password)
    tiene_numero = any(c.isdigit() for c in password)
    tiene_especial = any(c in string.punctuation for c in password)

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial

# Pruebas
print(validar_contraseña("HolaMundo123@"))  # True
print(validar_contraseña("holamundo"))  # False
print(validar_contraseña("Hola1234"))  # False (Falta caracter especial)
print(validar_contraseña("HOLA@123"))  # False (Falta minúscula)