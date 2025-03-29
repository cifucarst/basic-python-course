import hashlib
import re

def descifrar_md5(hash_md5: str, diccionario) -> str:
    """
    Intenta encontrar la contraseña original que produce un hash MD5 dado en un diccionario.
    """
    # Verifica que el hash sea un MD5 válido (32 caracteres hexadecimales)
    if not re.fullmatch(r"^[0-9a-fA-F]{32}$", hash_md5):
        return "Desconocido"

    for contrasena in diccionario:
        if hashlib.md5(contrasena.encode()).hexdigest() == hash_md5:
            return contrasena  # Devolvemos la contraseña encontrada

    return "No encontrada"

# Pruebas
hash_md5 = "5d41402abc4b2a76b9719d911017c592"  # MD5 de "hello"
diccionario = ["password", "123456", "hola123", "seguridad", "admin", "hello"]

print(descifrar_md5(hash_md5, diccionario))  # Debe devolver "hello"
print(descifrar_md5("no_es_un_hash_valido", diccionario))  # "Desconocido"
print(descifrar_md5("d41d8cd98f00b204e9800998ecf8427e", diccionario))  # "No encontrada" (hash de cadena vacía)