# Guardar y cargar objetos con pickle
# Usar pickle para almacenar objetos Python en un archivo binario.

# Código:


import pickle

# Guardar datos
datos = {"nombre": "Andrés", "edad": 25, "ciudad": "Bogotá"}
with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

# Cargar datos
with open("datos.pkl", "rb") as archivo:
    datos_cargados = pickle.load(archivo)

print(datos_cargados)