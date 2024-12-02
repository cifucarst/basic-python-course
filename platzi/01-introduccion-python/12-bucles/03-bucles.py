# control de iteraciones
# break
for num in range(10):
    if num == 5:
        break
    print(num)
# Salida:
# 0
# 1
# 2
# 3
# 4



# continue
for num in range(5):
    if num == 2:
        continue
    print(num)
# Salida:
# 0
# 1
# 3
# 4



# else en bucles
for num in range(5):
    print(num)
else:
    print("Bucle terminado sin interrupciones")
# Salida:
# 0
# 1
# 2
# 3
# 4
# Bucle terminado sin interrupciones



# con break
for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("Bucle terminado sin interrupciones")
# Salida:
# 0
# 1
# 2
