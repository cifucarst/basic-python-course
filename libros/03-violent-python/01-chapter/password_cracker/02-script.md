¡Perfecto! Vamos a mejorar este ataque de diccionario usando un enfoque más moderno. En lugar de depender de `crypt.crypt()` (que es antiguo y limitado), usaremos un enfoque **más compatible y fuerte** con contraseñas cifradas con algoritmos como:

- **MD5**
- **SHA-1**
- **SHA-256**
- **SHA-512**
- **bcrypt** (si quieres aún más seguridad)

---

## ✅ Versión moderna del ataque de diccionario

Usaremos `hashlib` para SHA-* y `bcrypt` si quieres probar con hashes más actuales.

### 🔐 Ejemplo con SHA-512 (`hashlib`)

```python
import hashlib

def hash_password_sha512(password):
    """Hash a password using SHA-512"""
    return hashlib.sha512(password.encode()).hexdigest()


def testPass(cryptPass):
    try:
        with open('dictionary.txt', 'r') as dictFile:
            for word in dictFile:
                word = word.strip()
                hashedWord = hash_password_sha512(word)
                if hashedWord == cryptPass:
                    print(f"[+] Found Password: {word}\n")
                    return
    except FileNotFoundError:
        print("[-] dictionary.txt not found.")
        return

    print("[-] Password Not Found.\n")


def main():
    try:
        with open('passwords_sha512.txt', 'r') as passFile:
            for line in passFile:
                if ":" in line:
                    user = line.split(':')[0]
                    cryptPass = line.split(':')[1].strip()
                    print(f"[*] Cracking Password For: {user}")
                    testPass(cryptPass)
    except FileNotFoundError:
        print("[-] passwords_sha512.txt not found.")


if __name__ == "__main__":
    main()
```

---

### 🧪 Archivo `passwords_sha512.txt` (ejemplo)
```txt
user1:9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
```

> Esa es la contraseña `hello` con hash SHA-512.

---

### ⚙️ Si quieres usar `bcrypt`

`bcrypt` es ideal para seguridad real porque incluye un *salt* y es lento (bueno para proteger contraseñas). Instálalo con:

```bash
pip install bcrypt
```

Y dime si quieres una versión de este script con `bcrypt` y te la preparo también.

---

¿Te gustaría que convierta contraseñas de texto plano en SHA-512 o bcrypt para hacer tus propias pruebas? ¿O que le agregue soporte para *multi-algoritmos*?