# 5. sys.version y sys.version_info
# sys.version devuelve la versión de Python como una cadena; sys.version_info devuelve una tupla con más detalles.

# Ejemplo práctico: Comprobar la versión de Python


import sys

print("Versión de Python:")
print(sys.version)

if sys.version_info >= (3, 9):
    print("Tu versión de Python es compatible con este programa.")
else:
    print("Actualiza a Python 3.9 o superior.")