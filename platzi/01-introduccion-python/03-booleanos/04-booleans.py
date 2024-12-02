# uso en estructuras condicionales

x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")


# operaciones combinadas
x = 10
y = 20
if x > 5 and y < 30:
    print("Ambas condiciones son ciertas")


# conversiones a booleanos
print(bool(0))         # False
print(bool(1))         # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True
