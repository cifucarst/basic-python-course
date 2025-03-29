# Ejercicio 2: Hashing de Contraseñas Débiles
# 📌 Objetivo: Crear un diccionario donde las claves sean contraseñas débiles y los valores sean sus hashes SHA-256.

# 🔹 Instrucciones:
# Dado el siguiente listado de contraseñas débiles:


# contraseñas = ["123456", "password", "qwerty", "admin", "letmein"]
# Usa dictionary comprehension y la librería hashlib para crear un diccionario con las contraseñas como claves y sus hashes SHA-256 como valores.

# 📌 Salida esperada (ejemplo con solo una clave):


# {
#     "123456": "e10adc3949ba59abbe56e057f20f883e",
#     "password": "5e884898da28047151d0e56f8dc62927",
#     ...
# }

import hashlib

contrasenas = ["123456", "password", "qwerty", "admin", "letmein"]

contrasena_hasheadas = {contrasena: hashlib.sha256(contrasena.encode()).hexdigest() for contrasena in contrasenas}
print(contrasena_hasheadas)