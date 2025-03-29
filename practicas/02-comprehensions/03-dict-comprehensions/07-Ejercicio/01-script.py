# Ejercicio 3: Detectar Contraseñas Débiles
# Dado un diccionario donde las claves son usuarios y los valores son sus contraseñas, crea un nuevo diccionario donde las contraseñas débiles (menos de 8 caracteres) sean marcadas como "Débil" y las demás como "Segura".

# 🔹 Entrada:

credenciales = {
    "usuario1": "123456",
    "usuario2": "segura123",
    "usuario3": "qwerty",
    "usuario4": "contraseñaLarga"
}
# 🔹 Salida esperada:

# {
#     "usuario1": "Débil",
#     "usuario2": "Segura",
#     "usuario3": "Débil",
#     "usuario4": "Segura"
# }

from typing import Dict

def mark_passwords(credenciales: Dict[str, str]) -> Dict[str, str]:

    if not isinstance(credenciales, dict):
        raise ValueError("El parámetro 'credenciales' debe ser un diccionario con nombre de usuario (str) contrasena (str)")
    
    if not all(isinstance(password, str)  for password in credenciales.values()):
        raise ValueError("Todos las contrasenas deben estar en texto plano")
    
    return {usuario: "❌Debil" if len(password) < 8 else '✅Segura' for usuario, password in credenciales.items()}
    
result = mark_passwords(credenciales)

print(f"Contrasenas de usuarios clasificadas como débiles y seguras")
for usuario, password in result.items():
    print(f"{usuario.ljust(15)} ➜ {password}")