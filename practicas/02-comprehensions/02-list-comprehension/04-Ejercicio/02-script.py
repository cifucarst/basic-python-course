from typing import Dict, List

def weak_passwords(users: Dict[str, str]) -> Dict[str, str]:
    """Filtra los usuarios con contraseñas débiles (menos de 8 caracteres)."""
    return {user: password for user, password in users.items() if len(password) < 8}

# Diccionario de usuarios y contraseñas
users = {
    "alice": "123456",
    "bob": "hunter2",
    "charlie": "password",
    "dave": "securePass123"
}

# Obtener contraseñas débiles
result = weak_passwords(users)

# Mostrar resultado
for user, password in result.items():
    print(f"{user} tiene una contraseña débil: {password}")