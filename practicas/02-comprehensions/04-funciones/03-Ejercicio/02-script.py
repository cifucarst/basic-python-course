import re

def identificar_hash(hash_str: str) -> str:
    # Expresión regular para verificar si el hash es hexadecimal
    if not re.fullmatch(r"^[0-9a-fA-F]+$", hash_str):
        return "Desconocido"

    # Identificar el tipo de hash basado en la longitud
    if len(hash_str) == 32:
        return "MD5"
    elif len(hash_str) == 40:
        return "SHA-1"
    elif len(hash_str) == 64:
        return "SHA-256"
    elif len(hash_str) == 128:
        return "SHA-512"
    else:
        return "Desconocido"

# Pruebas
print(identificar_hash("5d41402abc4b2a76b9719d911017c592"))  # MD5  
print(identificar_hash("2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"))  # SHA-1  
print(identificar_hash("d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2"))  # SHA-256  
print(identificar_hash("no_es_un_hash_valido"))  # Desconocido  
print(identificar_hash("5d41402abc4b2a76b9719d911017c59Z"))  # Desconocido (contiene 'Z', que no es hexadecimal)  