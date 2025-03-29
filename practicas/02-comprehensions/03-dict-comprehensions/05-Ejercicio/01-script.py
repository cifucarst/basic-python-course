# Ejercicio 1: Clasificación de Hashes
# Dado un diccionario con nombres de usuarios y sus contraseñas en texto plano, genera un nuevo diccionario donde las contraseñas estén cifradas con SHA-256.

# 🔹 Entrada:

# usuarios = {
#     "alice": "qwerty123",
#     "bob": "hunter2",
#     "charlie": "password",
#     "dave": "admin123"
# }
# 🔹 Salida esperada (Ejemplo, los hashes pueden variar):

# {
#     "alice": "ef92b778bafe771e89245b89ecbcfab...",
#     "bob": "a1f2c3d4e5b6a7d8c9e0...",
#     "charlie": "5f4dcc3b5aa765d61d8327deb882cf99...",
#     "dave": "21232f297a57a5a743894a0e4a801fc3..."
# }

from typing import Dict
import hashlib

def hashear_contrasenas(usuarios: Dict[str, str]) -> Dict[str, str]:
    """
    Devuelve un diccionario donde la contrasena de cada usuario es convertida a un hash seguro.
    """
    if not isinstance(usuarios, dict):
        raise ValueError("El parámetro usuarios debe ser un diccionario con usuario como clave y contrasena como valor")
    return {usuario: hashlib.sha256(contrasena.encode()).hexdigest() for usuario, contrasena in usuarios.items()}


usuarios = {
    "alice": "qwerty123",
    "bob": "hunter2",
    "charlie": "password",
    "dave": "admin123"
}

respuesta = hashear_contrasenas(usuarios)
for usuario, contrasena in respuesta.items():
    print(f"- {usuario} \t{contrasena}")