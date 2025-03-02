# Aplicaciones en el mundo real

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
respuesta = requests.get(url)

# Convertir respuesta JSON a diccionario de Python
datos = respuesta.json()
print(datos)

import json

# Almacenamiento de configuraciones: 
# Los archivos JSON se utilizan frecuentemente para guardar configuraciones de aplicaciones.

# Ejemplo:

configuracion = {
    "tema": "oscuro",
    "volumen": 80,
    "idioma": "español"
}

with open("config.json", "w") as archivo:
    json.dump(configuracion, archivo, indent=4)
