import hashlib
import warnings

def dynamic_hash(passwords, algorithm='sha256'):
    """
    Calcula los hashes de una lista de contraseñas usando el algoritmo especificado.

    Args:
        passwords (list | str): Una lista de contraseñas o una sola contraseña a hashear.
        algorithm (str): El algoritmo de hashing a usar (por defecto 'sha256').

    Returns:
        dict | str: Un diccionario con los hashes de las contraseñas o un string si solo se pasó una contraseña.
    """
    if not hasattr(hashlib, algorithm.lower()):
        raise ValueError(f"Algoritmo de hashing no válido: {algorithm}")

    # Si se pasa un solo string en lugar de una lista, conviértelo en una lista de un solo elemento
    if isinstance(passwords, str):
        return getattr(hashlib, algorithm.lower())(passwords.encode()).hexdigest()

    if not isinstance(passwords, list):
        raise TypeError("El parámetro 'passwords' debe ser una lista o un string.")

    hashes = {}

    for password in passwords:
        if password is None:
            warnings.warn("Se encontró una contraseña 'None'. Será ignorada.")
            continue
        try:
            hashes[password] = getattr(hashlib, algorithm.lower())(password.encode()).hexdigest()
        except Exception as e:
            warnings.warn(f"Error al calcular el hash de '{password}': {e}")

    return hashes

# Pruebas con una lista de contraseñas
passwords = ["password123", "contraseña456", "12345", None]

print(f"Hashes SHA-256: {dynamic_hash(passwords)}")
print(f"Hashes SHA-512: {dynamic_hash(passwords, 'sha512')}")
print(f"Hashes MD5: {dynamic_hash(passwords, 'md5')}")  # Algoritmo inseguro

# Prueba con un algoritmo inexistente (devolverá un error)
try:
    print(f"Hashes SHA-1024: {dynamic_hash(passwords, 'sha1024')}")
except ValueError as e:
    print(e)

# Prueba con un solo string en lugar de lista
print(f"Hash único SHA-256: {dynamic_hash('mypassword')}")