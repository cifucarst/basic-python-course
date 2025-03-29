# Ejercicio 5: Generar diccionarios de contraseñas únicas
# Tienes dos archivos con listas de contraseñas filtradas de distintas brechas de seguridad. Escribe un programa que:

# Identifique todas las contraseñas únicas entre ambos archivos.
# Encuentre las contraseñas que aparecen en ambos archivos (compartidas).
# 📌 Instrucciones:

# Simula dos archivos de contraseñas filtradas con listas en Python.
# Usa conjuntos para encontrar contraseñas únicas y compartidas.

# 🔹 Ejemplo de entrada:
# breach1 = {"password123", "qwerty", "123456", "letmein"}
# breach2 = {"123456", "password123", "admin", "welcome"}

# 🔹 Salida esperada:
# Contraseñas únicas: {'qwerty', 'letmein', 'admin', 'welcome'}
# Contraseñas compartidas: {'123456', 'password123'}


from typing import Set, Tuple

def find_unique_passwords(breach1: Set[str], breach2: Set[str]) -> Tuple[Set[str], Set[str]]:
    """Encuentra las contraseñas únicas en cada brecha y las que se comparten en ambas."""
    unique_passwords = breach1 ^ breach2  # Diferencia simétrica: contraseñas únicas en cada conjunto
    shared_passwords = breach1 & breach2  # Intersección: contraseñas que están en ambas brechas

    return unique_passwords, shared_passwords

# Datos de ejemplo
breach1 = {"password123", "qwerty", "123456", "letmein"}
breach2 = {"123456", "password123", "admin", "welcome"}

# Obtener resultados
unique, shared = find_unique_passwords(breach1, breach2)

# Imprimir de manera más clara
print(f"Contraseñas únicas: {unique}\nContraseñas compartidas: {shared}")