¡Perfecto! Vamos con la **opción 2: ataque de diccionario a contraseñas cifradas con SHA-256**, que es más común que SHA-512 en sistemas y aplicaciones web modernas.

---

## 🔐 OPCIÓN 2: SHA-256 con `hashlib`

### 📁 Estructura de archivos

#### `dictionary.txt`
Lista de contraseñas posibles:
```
123456
admin
letmein
qwerty
password
```

#### `passwords_sha256.txt`
Archivo con usuarios y contraseñas hasheadas en SHA-256:
```
user1:8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
```

> Esa es la contraseña `123456` hasheada con SHA-256.

---

### 🧠 Script: ataque con SHA-256

```python
import hashlib

def hash_password_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def test_pass(crypt_pass):
    try:
        with open('dictionary.txt', 'r') as dict_file:
            for word in dict_file:
                word = word.strip()
                hashed_word = hash_password_sha256(word)
                if hashed_word == crypt_pass:
                    print(f"[+] Found Password: {word}\n")
                    return
    except FileNotFoundError:
        print("[-] dictionary.txt not found.")
        return

    print("[-] Password Not Found.\n")

def main():
    try:
        with open('passwords_sha256.txt', 'r') as pass_file:
            for line in pass_file:
                if ":" in line:
                    user, crypt_pass = line.strip().split(":")
                    print(f"[*] Cracking Password For: {user}")
                    test_pass(crypt_pass)
    except FileNotFoundError:
        print("[-] passwords_sha256.txt not found.")

if __name__ == "__main__":
    main()
```

---

### 🧪 Herramienta para generar hash SHA-256

```python
import hashlib

def generate_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

print(generate_sha256("123456"))
```

---

¿Todo claro hasta aquí? Si estás listo, pasamos a la **opción 3: ataque de diccionario usando `bcrypt`**, que es más realista para entornos modernos como Linux, Django, etc. ¿Avanzamos?