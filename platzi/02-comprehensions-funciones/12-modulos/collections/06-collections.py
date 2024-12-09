# 6. ChainMap
# Une varios diccionarios en una sola vista para realizar búsquedas combinadas.

# Ejemplo: Combinar configuraciones


from collections import ChainMap

config_por_defecto = {"color": "azul", "tamaño": "mediano"}
config_usuario = {"tamaño": "grande", "tema": "oscuro"}

config_final = ChainMap(config_usuario, config_por_defecto)
print(config_final["color"])  # Salida: azul (valor por defecto)
print(config_final["tamaño"])  # Salida: grande (sobrescrito por el usuario)