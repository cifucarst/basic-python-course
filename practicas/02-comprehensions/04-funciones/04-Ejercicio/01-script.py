# Ejercicio 4: Fuerza Bruta de Hash MD5
# Crea una función en Python llamada descifrar_md5(hash_md5: str, diccionario: list) -> str que intente descifrar un hash MD5 usando un ataque de fuerza bruta con diccionario.

# ✅ La función debe recibir:
# 1️⃣ Un hash MD5 a descifrar.
# 2️⃣ Una lista de posibles contraseñas (diccionario).

# ✅ Debe devolver:

# La contraseña en texto plano si se encuentra en el diccionario.

# "No encontrada" si ninguna palabra coincide con el hash.

# Ejemplo de uso:

# diccionario = ["password", "123456", "hola123", "seguridad", "admin"]

# hash_md5 = "5d41402abc4b2a76b9719d911017c592"  # Corresponde a "hello"

# print(descifrar_md5(hash_md5, diccionario))  # "No encontrada"
# 💡 Pista: Usa la librería hashlib para calcular el MD5 de cada palabra y compararlo con el hash dado.

import re
import hashlib

def descifrar_md5(hash_md5: str, diccionario: list) -> str:
    """
    Intenta encontrar la contraseña original que produce un hash MD5 dado en un diccionario.
    """
    # Expresión regular para verificar si el hash es hexadecimal
    if not re.fullmatch(r"^[0-9a-fA-F]+$", hash_md5):
        return "Desconocido"

    if not isinstance(diccionario, list):
        raise ValueError("Debes ingresar una lista con las contraseñas")
    
    for contrasena in diccionario:
        if hashlib.md5(contrasena.encode()).hexdigest() == hash_md5:
            return "Encontrada"
    return "No Encontrada" 


hash_md5 = "5d41402abc4b2a76b9719d911017c592"  # Corresponde a "hello"
diccionario = ["password", "123456", "hola123", "seguridad", "admin"]

print(descifrar_md5(hash_md5, diccionario))