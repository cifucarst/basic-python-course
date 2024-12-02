mi_lista = []
print(mi_lista)  # []


# lista con elementos
numeros = [1, 2, 3, 4]
nombres = ["Ana", "Luis", "Carlos"]
mixta = [1, "Python", 3.14, True]

print(numeros)  # [1, 2, 3, 4]
print(nombres)  # ["Ana", "Luis", "Carlos"]
print(mixta)    # [1, "Python", 3.14, True]


# Acceder a elementos de una lista
colores = ["rojo", "verde", "azul"]
print(colores[0])  # "rojo"
print(colores[1])  # "verde"

# indices negativos
print(colores[-1])  # "azul"
print(colores[-2])  # "verde"


# modificar elementos
colores = ["rojo", "verde", "azul"]
colores[1] = "amarillo"
print(colores)  # ["rojo", "amarillo", "azul"]
