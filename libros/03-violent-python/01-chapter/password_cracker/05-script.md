¡Genial! Continuamos con la **opción 3: ataque de diccionario a contraseñas cifradas usando `bcrypt`**, que es muy utilizado hoy en día por su seguridad gracias al uso de *salts* aleatorios y su resistencia a ataques por fuerza bruta.

---

## 🔐 OPCIÓN 3: `bcrypt` (con hash + salt)

### 📦 Requisitos

Primero, asegúrate de tener el módulo `bcrypt` instalado:

```bash
pip install bcrypt
```

---

### ⚠️ Consideraciones de `bcrypt`

- A diferencia de SHA-256/SHA-512, **bcrypt genera un `salt` único por cada hash**.
- No puedes comparar hashes directamente. Debes usar `bcrypt.checkpw()`.

---

### 📁 Estructura de archivos

#### `dictionary.txt`
```txt
123456
admin
letmein
qwerty
password
```

#### `passwords_bcrypt.txt`
```txt
user1:$2b$12$VHmGz8n5O7UzJp4qzNLXuOW36Aj0BygmAvPy2e5trwsVXUnDoPKN6
```

Ese hash corresponde a `password`.

---

### 🧠 Script: ataque con `bcrypt`

```python
import bcrypt

def test_pass(crypt_pass):
    try:
        with open('dictionary.txt', 'r') as dict_file:
            for word in dict_file:
                word = word.strip().encode('utf-8')
                if bcrypt.checkpw(word, crypt_pass.encode('utf-8')):
                    print(f"[+] Found Password: {word.decode()}\n")
                    return
    except FileNotFoundError:
        print("[-] dictionary.txt not found.")
        return

    print("[-] Password Not Found.\n")

def main():
    try:
        with open('passwords_bcrypt.txt', 'r') as pass_file:
            for line in pass_file:
                if ":" in line:
                    user, crypt_pass = line.strip().split(":")
                    print(f"[*] Cracking Password For: {user}")
                    test_pass(crypt_pass)
    except FileNotFoundError:
        print("[-] passwords_bcrypt.txt not found.")

if __name__ == "__main__":
    main()
```

---

### 🧪 Cómo generar un hash `bcrypt` (para pruebas)

```python
import bcrypt

password = "password".encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
```

Esto imprimirá algo como:

```
$2b$12$VHmGz8n5O7UzJp4qzNLXuOW36Aj0BygmAvPy2e5trwsVXUnDoPKN6
```

---

¿Listo para la opción 4? Podemos ver `crypt` clásico de Unix con sal o `sha512crypt`, o incluso pasar a `argon2`, que es otro estándar moderno. ¿Cuál prefieres como siguiente paso?