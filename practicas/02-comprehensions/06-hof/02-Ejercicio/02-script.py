# 🧠 Bonus: Versión extendida con sal por usuario
# Si quieres ir un paso más allá, te puedo plantear una mejora opcional:

import hashlib
import uuid

def hash_con_salt(password: str) -> tuple:
    salt = uuid.uuid4().hex  # genera un "salt" único por contraseña
    hash_obj = hashlib.sha256((password + salt).encode())
    return salt, hash_obj.hexdigest()

passwords = [
        "admin123", 
        "letmein!", 
        "123456", 
        "P@ssw0rd", 
        "qwerty"
    ]

password_hasheadas = list(map(hash_con_salt, passwords))

print(f"hashes: {list(zip(passwords,password_hasheadas))}")