import hashlib

def dynamic_hash(passwords, algorithm='sha256'):
    """
    Calcula los hashes de una lista de contraseñas usando el algoritmo especificado.

    Args:
        passwords (list): Una lista de contraseñas a hashear.
        algorithm (str): El algoritmo de hashing a usar (por defecto 'sha256').

    Returns:
        dict: Un diccionario donde las claves son las contraseñas y los valores son sus hashes, o None si ocurre un error.
    """
    if not isinstance(passwords, list):
        print("Error: 'passwords' debe ser una lista.")
        return None

    hashes = {}
    algorithm_lower = algorithm.lower()

    if not hasattr(hashlib, algorithm_lower):
        print(f"Algoritmo de hashing no válido: {algorithm}")
        return None

    for password in passwords:
        if password is None:
            hashes[None]= None
            continue
        try:
            hashes[password] = getattr(hashlib, algorithm_lower)(password.encode()).hexdigest()
        except Exception as e:
            print(f"Error al calcular el hash de '{password}': {e}")
            return None

    return hashes

# Pruebas con una lista de contraseñas
passwords = ["password123", "contraseña456", "12345", None]

result_sha256 = dynamic_hash(passwords)
print(f"Hashes SHA-256: {result_sha256}")

result_sha512 = dynamic_hash(passwords, 'sha512')
print(f"Hashes SHA-512: {result_sha512}")

result_md5 = dynamic_hash(passwords, 'md5')
print(f"Hashes MD5: {result_md5}")

# Prueba con un algoritmo inexistente
result_fake = dynamic_hash(passwords, 'sha1024')
print(f"Hashes SHA-1024 (inexistente): {result_fake}")