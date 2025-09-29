# Bucles:
    # Escribe un programa que imprima todos los números pares del 1 al 50.

for i in range(51):
    if i % 2 == 0:
        print(i)

i = 0
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1  


# Mejoras


print("Usando for:")
for i in range(0, 51, 2):
    print(i)

print("\nUsando while:")
i = 0
while i <= 50:
    print(i)
    i += 2