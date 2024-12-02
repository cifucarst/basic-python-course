# Ejemplos prácticos
# Serializar datos de Python a JSON

import json

# Datos en formato Python
datos_python = {
    "nombre": "Andrés",
    "edad": 25,
    "ciudad": "Bogotá",
    "habilidades": ["Python", "JavaScript", "C++"]
}

# Convertir a JSON (serialización)
datos_json = json.dumps(datos_python, indent=4)
print(datos_json)


# salida json
{
    "nombre": "Andrés",
    "edad": 25,
    "ciudad": "Bogotá",
    "habilidades": ["Python", "JavaScript", "C++"]
}
