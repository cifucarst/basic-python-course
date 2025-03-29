import bcrypt
import json
import random
import string
from typing import Dict

# Lista de contraseñas comúnmente usadas
COMMON_PASSWORDS = {
    "123456", "password", "qwerty", "admin", "letmein", 
    "123456789", "welcome", "monkey", "football", "iloveyou"
}

# Función para generar una contraseña segura
def generar_contrasena_segura(longitud: int = 12) -> str:
    """Genera una contraseña segura aleatoria con la longitud especificada."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Función para verificar si una contraseña es débil
def es_contrasena_debil(password: str) -> bool:
    """Verifica si una contraseña es débil según ciertos criterios."""
    return (
        len(password) < 8 or
        password.lower() in COMMON_PASSWORDS or
        password.isnumeric() or
        password.isalpha() or
        not any(c.islower() for c in password) or
        not any(c.isupper() for c in password) or
        not any(c.isdigit() for c in password) or
        not any(c in string.punctuation for c in password)
    )

# Función para hashear contraseñas con bcrypt
def hashear_contrasena(password: str) -> str:
    """Devuelve el hash bcrypt de una contraseña."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

# Función para procesar credenciales y guardarlas en un archivo JSON
def procesar_credenciales(credenciales: Dict[str, str], longitud_contrasena: int = 12, archivo_salida: str = "usuarios_hashed.json") -> Dict[str, str]:
    """
    1️⃣ Clasifica contraseñas como seguras o débiles.  
    2️⃣ Si son seguras, se almacenan con bcrypt.  
    3️⃣ Si son débiles, se sugiere una nueva contraseña segura.  
    4️⃣ Guarda los hashes en un archivo JSON.  
    """
    if not isinstance(credenciales, dict):
        raise ValueError("El parámetro 'credenciales' debe ser un diccionario con nombre de usuario (str) y contraseña (str).")
    
    resultado = {}

    for usuario, password in credenciales.items():
        if es_contrasena_debil(password):
            nueva_contrasena = generar_contrasena_segura(longitud_contrasena)
            resultado[usuario] = {
                "estado": "❌ Débil",
                "sugerida": nueva_contrasena
            }
        else:
            hashed_password = hashear_contrasena(password)
            resultado[usuario] = {
                "estado": "✅ Segura",
                "hash": hashed_password
            }

    # Guardar en un archivo JSON
    with open(archivo_salida, "w") as file:
        json.dump(resultado, file, indent=4)
    
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

# Permitir al usuario elegir la longitud de las contraseñas seguras
longitud_personalizada = int(input("Ingrese la longitud de la contraseña segura (mínimo 8, por defecto 12): ") or 12)
longitud_personalizada = max(8, longitud_personalizada)  # Asegurar que la longitud sea al menos 8

# Procesar credenciales y guardar en JSON
resultados = procesar_credenciales(credenciales, longitud_personalizada)

# Imprimir resultados formateados
print("\nClasificación de contraseñas y sugerencias de seguridad:")
print("*" * 80)
for usuario, data in resultados.items():
    if "sugerida" in data:
        print(f"{usuario.ljust(15)} ➜ {data['estado']} | Sugerida: {data['sugerida']}")
    else:
        print(f"{usuario.ljust(15)} ➜ {data['estado']} | Hash almacenado en JSON ✅")

print("\n✅ Los hashes han sido guardados en 'usuarios_hashed.json'")