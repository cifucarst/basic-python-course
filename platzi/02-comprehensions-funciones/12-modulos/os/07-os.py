# 7. os.path
# El submódulo os.path proporciona herramientas para trabajar con rutas.

# Funciones principales:
# os.path.join(path1, path2): Une rutas de manera segura.
# os.path.exists(path): Verifica si una ruta existe.
# os.path.isfile(path): Verifica si es un archivo.
# os.path.isdir(path): Verifica si es un directorio.

# Ejemplo práctico: Trabajar con rutas


import os

ruta_base = os.getcwd()
archivo = "archivo_ejemplo.txt"
ruta_completa = os.path.join(ruta_base, archivo)

print("Ruta completa:", ruta_completa)

# Verificar si existe
if not os.path.exists(ruta_completa):
    print(f"La ruta '{ruta_completa}' no existe.")
else:
    print(f"La ruta '{ruta_completa}' existe.")