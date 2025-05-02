# Ejercicio 1: Hashing con Lambda
# Crea una función lambda que reciba un string y devuelva su hash SHA-256.

# Pistas:

# Usa el módulo hashlib.

# Recuerda que debes codificar el string a bytes antes de calcular el hash.

# Ejemplo de uso esperado:


# hash_sha256("password123")
# Salida esperada (hash en hexadecimal):


# ef92b778bafe771e89245b89ecbcdfb2d0892e04ddbf0c6d947b0c0dfb1ba3a9

import hashlib

hash_password = lambda password: hashlib.sha256(password.encode()).hexdigest()

result = hash_password("password123")
print(result)