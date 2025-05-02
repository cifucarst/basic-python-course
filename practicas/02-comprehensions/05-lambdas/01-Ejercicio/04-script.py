import hashlib

# Función lambda mejorada para evitar errores con algoritmos inválidos
dynamic_hash = lambda password, algorithm='sha256': (
    getattr(hashlib, algorithm.lower())(password.encode()).hexdigest()
    if password and hasattr(hashlib, algorithm.lower())
    else None
)

# Pruebas con diferentes algoritmos
password = "password123"

result_sha256 = dynamic_hash(password)
print(f"SHA-256: {result_sha256}")

result_sha512 = dynamic_hash(password, 'sha512')
print(f"SHA-512: {result_sha512}")

result_md5 = dynamic_hash(password, 'md5')  # Algoritmo inseguro
print(f"MD5: {result_md5}")

# Prueba con un algoritmo inexistente
result_fake = dynamic_hash(password, 'sha1024')
print(f"SHA-1024 (inexistente): {result_fake}")