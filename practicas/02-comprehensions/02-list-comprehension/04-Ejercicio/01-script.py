# Ejercicio 4: Detectar usuarios con contraseñas débiles
# Dado un diccionario con usuarios y sus contraseñas, usa list comprehension para obtener una lista de usuarios que usan contraseñas débiles ("123456", "password", "qwerty").
from typing import Dict, List

def weak_passwords(users: Dict)-> List:
    return [password for password in users.values() if len(password) <= 7]


users = {
    "alice": "123456",
    "bob": "hunter2",
    "charlie": "password",
    "dave": "securePass123"
}

result = weak_passwords(users)
print(result)