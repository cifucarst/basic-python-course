# 6. os.environ
# Devuelve un diccionario con las variables de entorno del sistema.

# Ejemplo práctico: Leer y usar variables de entorno

import os

print("Variables de entorno:")
for clave, valor in os.environ.items():
    print(f"{clave} = {valor}")

# Acceder a una variable específica
usuario = os.environ.get("USER", "Usuario desconocido")
print(f"Usuario actual: {usuario}")