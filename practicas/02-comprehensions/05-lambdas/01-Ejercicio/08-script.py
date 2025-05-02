# 🎯 Siguiente desafío (Nivel CTF):
# Agrega una funcionalidad que permita comparar los hashes generados con un hash objetivo, para hacer un ataque de diccionario inverso y encontrar la contraseña original.

# Ejemplo:

# target_hash = 'ef92b778bafe771e89245b89ecbcdfb2d0892e04ddbf0c6d947b0c0dfb1ba3a9'
# Tu función debe devolver: "password123" si está en el diccionario.

import warnings
import hashlib
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
    

def crack_hash(target_hash, passwords, algorithm='sha256'):
    """
    Intenta encontrar la contraseña original comparando hashes generados con un hash objetivo.

    Args:
        target_hash (str): Hash objetivo que se desea romper.
        passwords (list | str): Lista de contraseñas o ruta a archivo con contraseñas.
        algorithm (str): Algoritmo de hashing usado para el hash objetivo.

    Returns:
        str | None: Contraseña original si se encuentra, de lo contrario None.
    """
    # Validar algoritmo
    if not hasattr(hashlib, algorithm.lower()):
        raise ValueError(f"Algoritmo de hashing no válido: {algorithm}")

    # Si se pasa un archivo, lo abrimos
    if isinstance(passwords, str) and os.path.exists(passwords):
        passwords = read_file(passwords)

    if not isinstance(passwords, list):
        raise TypeError("Se espera una lista de contraseñas o un archivo válido.")

    hash_func = getattr(hashlib, algorithm.lower())

    for password in passwords:
        if password is None:
            continue
        try:
            hashed = hash_func(password.encode()).hexdigest()
            print(f"Probando: '{password}' → {hashed}")  # <--- DEBUG
            if hashed == target_hash:
                print("[+] ¡Match encontrado!")
                return password
        except Exception as e:
            warnings.warn(f"Error procesando '{password}': {e}")



# Ejemplos de uso

target = 'ef92b778bafe771e89245b89ecbcdfb2d0892e04ddbf0c6d947b0c0dfb1ba3a9'  # hash de 'password123'
passwords = ["12345", "admin", "password123", "root"]

result = crack_hash(target, passwords, 'sha256')
if result:
    print(f"[+] Contraseña encontrada: {result}")
else:
    print("[-] Contraseña no encontrada en el diccionario.")
