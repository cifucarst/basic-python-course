# operaciones comunes

# longitud
colores = ["rojo", "verde", "azul"]
print(len(colores))  # 3


# anadir elementos
colores.append("morado")
print(colores)  # ["rojo", "verde", "azul", "morado"]

colores.extend(["negro", "blanco"])
print(colores)  # ["rojo", "verde", "azul", "morado", "negro", "blanco"]


# insertar elementos en una posicion especifica
colores.insert(1, "naranja")
print(colores)  # ["rojo", "naranja", "verde", "azul", "morado", "negro", "blanco"]


# Eliminar elementos
colores.remove("verde")
print(colores)  # ["rojo", "naranja", "azul", "morado", "negro", "blanco"]

colores.pop(2)
print(colores)  # ["rojo", "naranja", "morado", "negro", "blanco"]

colores.clear()
print(colores)  # []


# 