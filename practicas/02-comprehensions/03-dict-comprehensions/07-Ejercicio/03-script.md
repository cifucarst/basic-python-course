Aquí tienes el código mejorado con las tres funcionalidades adicionales:  

1️⃣ **Valida mayúsculas, minúsculas y caracteres especiales.**  
2️⃣ **Sugiere una contraseña segura cuando una sea débil.**  
3️⃣ **Hashea las contraseñas seguras antes de almacenarlas.**  

```python
import hashlib
import random
import string
from typing import Dict

# Lista de contraseñas comúnmente usadas
COMMON_PASSWORDS = {
    "123456", "password", "qwerty", "admin", "letmein", 
    "123456789", "welcome", "monkey", "football", "iloveyou"
}

def generar_contrasena_segura(longitud: int = 12) -> str:
    """Genera una contraseña segura aleatoria."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def es_contrasena_debil(password: str) -> bool:
    """Verifica si una contraseña es débil según ciertos criterios."""
    return (
        len(password) < 8 or  # Longitud menor a 8
        password.lower() in COMMON_PASSWORDS or  # Contraseña común
        password.isnumeric() or  # Solo números
        password.isalpha() or  # Solo letras
        not any(c.islower() for c in password) or  # Sin minúsculas
        not any(c.isupper() for c in password) or  # Sin mayúsculas
        not any(c.isdigit() for c in password) or  # Sin números
        not any(c in string.punctuation for c in password)  # Sin caracteres especiales
    )

def clasificar_y_hashear_contrasenas(credenciales: Dict[str, str]) -> Dict[str, str]:
    """
    Clasifica las contraseñas como seguras o débiles.
    Si son seguras, se almacenan con hashing SHA-256.
    Si son débiles, se sugiere una nueva contraseña segura.
    """
    if not isinstance(credenciales, dict):
        raise ValueError("El parámetro 'credenciales' debe ser un diccionario con nombre de usuario (str) y contraseña (str).")
    
    resultado = {}
    
    for usuario, password in credenciales.items():
        if es_contrasena_debil(password):
            nueva_contrasena = generar_contrasena_segura()
            resultado[usuario] = f"❌ Débil | Sugerencia: {nueva_contrasena}"
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            resultado[usuario] = f"✅ Segura | Hash: {hashed_password}"

    return resultado

# Diccionario de credenciales de ejemplo
credenciales = {
    "alice": "qwerty123",
    "bob": "hunter2",
    "charlie": "password",
    "dave": "Admin123!",
    "eve": "abcdefg",
    "mallory": "987654321",
    "oscar": "SuperSecurePass1!"
}

# Clasificar y procesar contraseñas
resultados = clasificar_y_hashear_contrasenas(credenciales)

# Imprimir resultados formateados
print("Clasificación de contraseñas y sugerencias de seguridad:")
print("*" * 70)
for usuario, estado in resultados.items():
    print(f"{usuario.ljust(15)} ➜ {estado}")
```

---

### **🚀 ¿Qué incluye esta versión?**
✅ **Validación avanzada:**  
✔ Comprueba si la contraseña tiene minúsculas, mayúsculas, números y caracteres especiales.  
✔ Detecta si es una contraseña comúnmente usada.  

✅ **Generación automática de contraseñas seguras:**  
✔ Si una contraseña es débil, se sugiere una aleatoria de 12 caracteres.  

✅ **Hasheo de contraseñas seguras:**  
✔ Si la contraseña es segura, se convierte a SHA-256 antes de almacenarla.  

---

### **Ejemplo de salida**:
```
Clasificación de contraseñas y sugerencias de seguridad:
**********************************************************************
alice           ➜ ❌ Débil | Sugerencia: rT8#vBk2p!Lc
bob             ➜ ❌ Débil | Sugerencia: m4$Yq2!zKtXf
charlie         ➜ ❌ Débil | Sugerencia: X!h5oM@3vT7a
dave            ➜ ✅ Segura | Hash: 32dcb88a3d6e6a...
eve             ➜ ❌ Débil | Sugerencia: zP#3t7V!yMqX
mallory         ➜ ❌ Débil | Sugerencia: Wq8X#M!2vT3o
oscar           ➜ ✅ Segura | Hash: 3b6d1c4f8f7e9...
```

---

### **📌 ¿Qué podríamos mejorar aún más?**
🔹 **Guardar los hashes en un archivo JSON o base de datos** en lugar de imprimirlos.  
🔹 **Permitir que el usuario elija la longitud de la contraseña segura.**  
🔹 **Usar una función más segura como `bcrypt` en lugar de SHA-256 para almacenar los hashes.**  

Si quieres seguir mejorando el script, dime qué aspecto te gustaría trabajar. 🚀