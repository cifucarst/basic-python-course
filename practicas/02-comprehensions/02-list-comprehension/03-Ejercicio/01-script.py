# Ejercicio 3: Convertir contraseñas en hashes SHA256

# Dada una lista de contraseñas filtradas en una brecha de seguridad, usa list comprehension y la librería hashlib para convertirlas en hashes SHA256.

# import hashlib

# passwords = ["admin123", "qwerty", "password", "hunter2"]


import hashlib
from typing import List

def convertir_contrasena_a_hash(passwords: List[str]) -> List[str]:
    return [hashlib.sha256(password.encode()).hexdigest() for password in passwords]

passwords = ["admin123", "qwerty", "password", "hunter2"]
print(convertir_contrasena_a_hash(passwords))