# Ejercicio 3: Analizador de Hashes
# Crea una función en Python llamada identificar_hash(hash_str: str) -> str que reciba un hash y determine qué tipo de algoritmo lo generó.

# Los tipos de hash que debes detectar:
# MD5 → 32 caracteres hexadecimales

# SHA-1 → 40 caracteres hexadecimales

# SHA-256 → 64 caracteres hexadecimales

# SHA-512 → 128 caracteres hexadecimales

# Si el hash no coincide con ninguno, devuelve "Desconocido".

# Ejemplo de uso:

# print(identificar_hash("5d41402abc4b2a76b9719d911017c592"))  # MD5  
# print(identificar_hash("2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"))  # SHA-1  
# print(identificar_hash("d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2"))  # SHA-256  
# print(identificar_hash("no_es_un_hash_valido"))  # Desconocido  

def identificar_hash(hash_str: str) -> str:
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
    
print(identificar_hash("5d41402abc4b2a76b9719d911017c592"))  # MD5  
print(identificar_hash("2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"))  # SHA-1  
print(identificar_hash("d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2"))  # SHA-256  
print(identificar_hash("no_es_un_hash_valido"))  # Desconocido