¡Excelente! Vamos a hacerlo paso a paso. Comenzamos con la primera opción: **ataque de diccionario a contraseñas cifradas con SHA-512**, usando `hashlib`.

---

## 🔐 OPCIÓN 1: SHA-512 con `hashlib`

### 📁 Estructura de archivos

#### `dictionary.txt`
Lista de posibles contraseñas (una por línea), por ejemplo:
```
123456
admin
hello
qwerty
password
```

#### `passwords_sha512.txt`
Usuarios con sus contraseñas hasheadas (SHA-512):
```
user1:9b71d224bd62f3785d96d46ad3ea3d73319b8d365ab7b8e7c5f4c1c8d6c4c1df212e5d1f1cbe0bf04e3d6aca59cd8a17f101ff8a353ef1e4b74f16c04c1c8f3b
```
> Esa es la contraseña `123456` hasheada con SHA-512.

Puedes generar hashes como ese usando Python (te muestro más abajo cómo).

---

### 🧠 Script: ataque con SHA-512

```python
import hashlib

def hash_password_sha512(password):
    return hashlib.sha512(password.encode()).hexdigest()

def test_pass(crypt_pass):
    try:
        with open('dictionary.txt', 'r') as dict_file:
            for word in dict_file:
                word = word.strip()
                hashed_word = hash_password_sha512(word)
                if hashed_word == crypt_pass:
                    print(f"[+] Found Password: {word}\n")
                    return
    except FileNotFoundError:
        print("[-] dictionary.txt not found.")
        return

    print("[-] Password Not Found.\n")

def main():
    try:
        with open('passwords_sha512.txt', 'r') as pass_file:
            for line in pass_file:
                if ":" in line:
                    user, crypt_pass = line.strip().split(":")
                    print(f"[*] Cracking Password For: {user}")
                    test_pass(crypt_pass)
    except FileNotFoundError:
        print("[-] passwords_sha512.txt not found.")

if __name__ == "__main__":
    main()
```

---

### 🧪 Herramienta auxiliar: generar hash SHA-512 en Python

Si quieres generar tus propios hashes para pruebas, puedes usar este código:

```python
import hashlib

def generate_sha512(password):
    return hashlib.sha512(password.encode()).hexdigest()

print(generate_sha512("123456"))
```

---

Cuando estés listo, pasamos a:

➡️ **Opción 2: ataque de diccionario usando SHA-256**  
¿Te gustaría esa como siguiente paso? ¿O prefieres ir directo a `bcrypt`?