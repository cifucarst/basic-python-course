# Funciones generadoras integradas

# Python ofrece funciones generadoras como:

# range(): Genera una secuencia de números.
# enumerate(): Proporciona un índice junto con el valor.
# zip(): Combina múltiples iterables.
# map() y filter(): Aplica funciones a iterables.

# Ejemplo de zip()
nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 35]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
# Salida:
# Ana tiene 25 años
# Luis tiene 30 años
# Pedro tiene 35 años
