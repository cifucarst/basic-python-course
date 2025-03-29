from typing import Dict, Tuple
import hashlib
import hmac
import os

def hashear_contrasenas(usuarios: Dict[str, str]) -> Dict[str, Tuple[str, str]]:
    """
    Devuelve un diccionario donde la contraseña de cada usuario es convertida a un hash seguro con salt.
    """
    if not isinstance(usuarios, dict):
        raise ValueError("El parámetro usuarios debe ser un diccionario con usuario como clave y contraseña como valor.")
    
    try:
        return {
            usuario: (
                (salt := os.urandom(16)).hex(),  # Genera un salt aleatorio de 16 bytes
                hmac.new(salt, contrasena.encode(), hashlib.sha256).hexdigest()  # Hash con salt
            )
            for usuario, contrasena in usuarios.items()
        }
    except Exception as e:
        print(f"Error al hashear contraseñas: {e}")
        return {}

# Diccionario de usuarios con contraseñas en texto plano
usuarios = {
    "alice": "qwerty123",
    "bob": "hunter2",
    "charlie": "password",
    "dave": "admin123"
}

# Obtener los hashes
respuesta = hashear_contrasenas(usuarios)

# Imprimir resultados de manera formateada
print("\nUsuarios con contraseñas hasheadas (salt + hash):")
print("-" * 80)
for usuario, (salt, contrasena) in respuesta.items():
    print(f"Usuario: {usuario}\nSalt: {salt}\nHash: {contrasena}\n" + "-" * 80)