# Condicionales:
#     Pide al usuario su edad.
#     Si tiene menos de 18, muestra “Eres menor de edad”.
#     Si tiene entre 18 y 65, muestra “Eres adulto”.
#     Si tiene más de 65, muestra “Eres adulto mayor”.

age = float(input("Cuantos anos tienes? "))

if age < 18:
    print('Eres menor de edad')
elif age >= 18 and age < 65:
    print('Eres adulto')
elif age >= 65:
    print('Eres adulto mayor')
else:
    print('Wrong! Invalid age')



# Mejora por chat gpt

age = int(input("¿Cuántos años tienes? "))

if age < 0:
    print("Edad inválida")
elif age < 18:
    print("Eres menor de edad")
elif age <= 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")
