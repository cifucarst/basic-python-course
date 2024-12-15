# Ejemplo avanzado: JSON anidado
# Trabajar con JSON que contiene estructuras complejas, como listas dentro de diccionarios.

import json

# JSON con estructura anidada
json_anidado = '''
{
    "curso": "Python avanzado",
    "estudiantes": [
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Luis", "edad": 24},
        {"nombre": "Carla", "edad": 23}
    ],
    "activo": true
}
'''

# Convertir JSON a Python
datos = json.loads(json_anidado)

# Acceder a elementos específicos
print(datos["curso"])  # Salida: Python avanzado
print(datos["estudiantes"][1]["nombre"])  # Salida: Luis
