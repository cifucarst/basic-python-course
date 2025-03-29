import hashlib
from typing import List

def hash_passwords(passwords: List[str]) -> List[str]:
    """Convierte una lista de contraseñas en sus respectivos hashes SHA-256."""
    return [hashlib.sha256(password.encode()).hexdigest() for password in passwords]

# Lista de contraseñas filtradas
passwords = ["admin123", "qwerty", "password", "hunter2"]

# Generar los hashes
hashed_passwords = hash_passwords(passwords)

# Imprimir resultados
for password, hashed in zip(passwords, hashed_passwords):
    print(f"{password} -> {hashed}")