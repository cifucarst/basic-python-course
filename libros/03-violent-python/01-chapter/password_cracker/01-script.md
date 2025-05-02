Gracias por compartir otro script del libro *Violent Python*. Este es un **script clásico de ataque de diccionario** contra contraseñas cifradas con `crypt`. Vamos a migrarlo a **Python 3**, corrigiendo varios puntos:

---

### 🛠 Errores en el script original:

- Comillas incorrectas (`‘’`, `“”`) → deben ser `'` o `"`
- `print` de Python 2
- Uso de `crypt.crypt()` que puede no funcionar igual dependiendo del sistema operativo (está disponible en Linux)
- Indentación faltante

---

### ✅ Versión migrada a Python 3:

```python
import crypt

def testPass(cryptPass):
    salt = cryptPass[:2]
    try:
        with open('dictionary.txt', 'r') as dictFile:
            for word in dictFile:
                word = word.strip()
                cryptWord = crypt.crypt(word, salt)
                if cryptWord == cryptPass:
                    print(f"[+] Found Password: {word}\n")
                    return
    except FileNotFoundError:
        print("[-] dictionary.txt not found.")
        return

    print("[-] Password Not Found.\n")


def main():
    try:
        with open('passwords.txt', 'r') as passFile:
            for line in passFile:
                if ":" in line:
                    user = line.split(':')[0]
                    cryptPass = line.split(':')[1].strip()
                    print(f"[*] Cracking Password For: {user}")
                    testPass(cryptPass)
    except FileNotFoundError:
        print("[-] passwords.txt not found.")


if __name__ == "__main__":
    main()
```

---

### 📁 Estructura de los archivos que debe tener:

**`passwords.txt`**  
Debe tener líneas como:
```
user1:50.jPgLzVirk6
user2:HX4HHU2qxd6fE
```

**`dictionary.txt`**  
Debe tener palabras en texto plano, como:
```
123456
admin
password
qwerty
letmein
```

---

### 🐧 Nota sobre `crypt.crypt()` en Linux

Este script solo funcionará en sistemas tipo UNIX (como Ubuntu) donde la función `crypt.crypt()` esté disponible. Si estás en Windows, esa función no está soportada.

---

¿Quieres que te ayude a mejorar este ataque de diccionario, por ejemplo usando wordlists grandes (como `rockyou.txt`) o adaptarlo a contraseñas con *hashes modernos* como SHA-512?