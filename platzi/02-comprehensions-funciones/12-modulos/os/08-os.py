# 8. os.system()
# Ejecuta un comando del sistema operativo desde Python.

# Ejemplo práctico: Ejecutar comandos de sistema


import os

# Comando para listar el contenido del directorio actual
comando = "dir" if os.name == "nt" else "ls"
os.system(comando)