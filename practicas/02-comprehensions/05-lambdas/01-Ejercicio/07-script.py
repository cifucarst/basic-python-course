# 🎯 Siguiente desafío:
# Modifica la función para que también acepte archivos con contraseñas (uno por línea) y devuelva sus hashes.

# ¡Espero tu solución! 🚀

import hashlib
import warnings
import os

def read_file(file_path):
    passwords = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                for line in f:
                    passwords.append(str(line.strip()))
            return passwords
        except Exception as e:
            warnings.warn(f"Error al leer el archivo '{file_path}': {e}")
            return None
    else:
        warnings.warn(f"El archivo '{file_path}' no existe.")
        return None

def dynamic_hash(passwords, algorithm='sha256'):
    if not hasattr(hashlib, algorithm.lower()):
        raise ValueError(f"Algoritmo de hashing no válido: {algorithm}")

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

# ---- Pruebas ----

passwords = ["password123", "contraseña456", "12345", None]
print(f"Hashes SHA-256: {dynamic_hash(passwords)}")
print(f"Hashes SHA-512: {dynamic_hash(passwords, 'sha512')}")
print(f"Hashes MD5: {dynamic_hash(passwords, 'md5')}")

print("\nProbando con un algoritmo inexistente:")
try:
    print(f"Hashes SHA-1024: {dynamic_hash(passwords, 'sha1024')}")
except ValueError as e:
    print(e)

print("\nHashear una única contraseña:")
print(f"Hash único SHA-256: {dynamic_hash('mypassword')}")

print("\nContraseñas leídas desde un archivo externo (ej. rockyou.txt):")
passwords_from_file = read_file("passwords.txt")
if passwords_from_file:
    print(f"Hashes from file in SHA-256: {dynamic_hash(passwords_from_file)}")
else:
    print("No se procesaron contraseñas del archivo.")