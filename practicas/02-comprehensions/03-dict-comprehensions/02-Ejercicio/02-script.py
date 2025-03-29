import hashlib

def generar_hashes(contrasenas):
    """Devuelve un diccionario con las contraseñas y sus hashes SHA-256."""
    return {pwd: hashlib.sha256(pwd.encode()).hexdigest() for pwd in contrasenas}

# Lista de contraseñas débiles
contrasenas = ["123456", "password", "qwerty", "admin", "letmein"]

# Generar y mostrar los hashes
hashes = generar_hashes(contrasenas)
for clave, valor in hashes.items():
    print(f"{clave}: {valor}")