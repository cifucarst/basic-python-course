import hashlib

# Función lambda para calcular el hash SHA-256 de una contraseña
hash_sha256 = lambda password: hashlib.sha256(password.encode()).hexdigest() if password else None

# Prueba con un ejemplo
result = hash_sha256("password123")
print(result)