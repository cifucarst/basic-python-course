# 3. sys.path
# Es una lista que contiene las rutas donde Python busca los módulos al importar.

# Ejemplo práctico: Agregar una nueva ruta para importar módulos personalizados


import sys

print("Rutas actuales para buscar módulos:")
for path in sys.path:
    print(path)

# Agregar una nueva ruta
sys.path.append("/ruta/a/tu/modulo")
print("\nNueva ruta agregada:")
print(sys.path[-1])