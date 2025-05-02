import hashlib

# Función lambda modificada para aceptar un algoritmo de hashing como parámetro
dinamyc_hash = lambda password, algorithm='sha256': getattr(hashlib, algorithm)(password.encode()).hexdigest() if password else None

# Pruebas con diferentes algoritmos
password = "password123"

result_sha256 = dinamyc_hash(password)
print(f"SHA-256: {result_sha256}")

result_sha512 = dinamyc_hash(password, 'sha512')
print(f"SHA-512: {result_sha512}")

result_md5 = dinamyc_hash(password, 'md5')
# algoritmo inseguro
print(f"MD5: {result_md5}")