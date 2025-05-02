# ✅ Ejercicio 2: Hashing de contraseñas con funciones de orden superior
# 🕵️‍♂️ Contexto:
# En un pentest estás revisando una base de datos con contraseñas en texto plano (algo que nunca debería pasar). Tu objetivo es simular cómo se deben proteger esas contraseñas usando hashing. Queremos aplicar SHA-256 a cada contraseña usando map() y una función personalizada.

# 🧩 Instrucciones:
# Crea una función llamada hash_password(password: str) -> str que:

# Acepte una contraseña en texto plano.

# Devuelva su hash SHA-256 como una cadena hexadecimal.

# Usa map() junto con hash_password para transformar una lista de contraseñas en una lista de hashes.

# Imprime la lista de contraseñas hasheadas.

# 🔐 Datos de ejemplo:
    # passwords = [
    #     "admin123", 
    #     "letmein!", 
    #     "123456", 
    #     "P@ssw0rd", 
    #     "qwerty"
    # ]
# 🧠 Tips:
    # Usa el módulo hashlib de Python.
    # Usa .hexdigest() para obtener el hash como string hexadecimal.

import hashlib

def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise ValueError("Debes ingresar la contrasena en texto plano (str)")
    
    return hashlib.sha256(password.encode()).hexdigest()


passwords = [
        "admin123", 
        "letmein!", 
        "123456", 
        "P@ssw0rd", 
        "qwerty"
    ]

password_hasheadas = list(map(hash_password, passwords))

print(f"hashes: {list(zip(passwords,password_hasheadas))}")