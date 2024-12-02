# Ejemplos practicos

# sin parentesis

resultado = 2 + 3 * 4 ** 2
print(resultado)  # 50
# Se evalúa así:
# 1. Exponentes: 4 ** 2 = 16
# 2. Multiplicación: 3 * 16 = 48
# 3. Suma: 2 + 48 = 50


# con parentesis para modificar la presedencia

resultado = (2 + 3) * (4 ** 2)
print(resultado)  # 80
# Se evalúa así:
# 1. Paréntesis: (2 + 3) = 5 y (4 ** 2) = 16
# 2. Multiplicación: 5 * 16 = 80


# combinacion de operadores

resultado = 10 // 3 * 2 ** 3 - 4 % 2
print(resultado)  # 26
# Se evalúa así:
# 1. Exponentes: 2 ** 3 = 8
# 2. División entera: 10 // 3 = 3
# 3. Multiplicación: 3 * 8 = 24
# 4. Módulo: 4 % 2 = 0
# 5. Resta: 24 - 0 = 24