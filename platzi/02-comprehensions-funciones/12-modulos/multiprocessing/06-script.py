import multiprocessing
import hashlib

def crack_hash(password):
    hash_obj = hashlib.sha256(password.encode())
    hashed_password = hash_obj.hexdigest()
    
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd60492f1788b2df8c6"  # hash de "password"
    
    if hashed_password == target_hash:
        print(f"[+] Contraseña encontrada: {password}")
        return True
    return False

if __name__ == "__main__":
    wordlist = ["123456", "qwerty", "password", "admin", "welcome"]
    
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(crack_hash, wordlist)

    if any(results):
        print("Ataque exitoso.")
    else:
        print("No se encontró la contraseña.")