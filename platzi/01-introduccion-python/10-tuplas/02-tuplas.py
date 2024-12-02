# Acceso y manipulación de elementos
# Acceso por índice

mi_tupla = (10, 20, 30, 40)
print(mi_tupla[0])  # 10
print(mi_tupla[-1])  # 40 (último elemento)


# Slicing (rebanado)
mi_tupla = (10, 20, 30, 40, 50)
print(mi_tupla[1:4])  # (20, 30, 40)


# Desempaquetado
mi_tupla = (1, 2, 3)
a, b, c = mi_tupla
print(a, b, c)  # 1 2 3

# Usar el operador * para desempaquetar parcialmente
mi_tupla = (1, 2, 3, 4, 5)
a, *resto, e = mi_tupla
print(a, resto, e)  # 1 [2, 3, 4] 5
