from typing import Dict

# Lista de contraseñas comúnmente usadas
COMMON_PASSWORDS = {"123456", "password", "qwerty", "admin", "letmein", "123456789", "welcome", "monkey", "football"}

def mark_passwords(credenciales: Dict[str, str]) -> Dict[str, str]:
    """
    Clasifica las contraseñas en seguras o débiles según ciertos criterios.
    """
    if not isinstance(credenciales, dict):
        raise ValueError("El parámetro 'credenciales' debe ser un diccionario con nombre de usuario (str) y contraseña (str).")
    
    if not all(isinstance(password, str) for password in credenciales.values()):
        raise ValueError("Todas las contraseñas deben estar en formato de texto plano.")

    def is_weak(password: str) -> bool:
        """Verifica si una contraseña es débil según diferentes criterios."""
        return (
            len(password) < 8 or  # Longitud menor a 8
            password.lower() in COMMON_PASSWORDS or  # Contraseña común
            password.isnumeric() or  # Solo números
            password.isalpha()  # Solo letras
        )

    return {usuario: "❌ Débil" if is_weak(password) else "✅ Segura" for usuario, password in credenciales.items()}

# Diccionario de credenciales de ejemplo
credenciales = {
    "alice": "qwerty123",
    "bob": "hunter2",
    "charlie": "password",
    "dave": "admin123",
    "eve": "abcdefg",
    "mallory": "987654321",
    "oscar": "SuperSecurePass1!"
}

# Clasificar contraseñas
result = mark_passwords(credenciales)

# Imprimir resultados formateados
print("Clasificación de contraseñas por seguridad:")
print("*" * 45)
for usuario, seguridad in result.items():
    print(f"{usuario.ljust(15)} ➜ {seguridad}")