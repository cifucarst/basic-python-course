# Nivel Intermedio (Listas, Diccionarios y Funciones)

# Listas y funciones:
#     Crea una función llamada filtrar_pares que reciba una lista de números y devuelva una nueva lista solo con los números pares.
#     Prueba la función con la lista [3, 4, 7, 10, 15, 20].

def filtrar_pares(pares):
    resultado = []
    for i in pares:
        if i % 2 == 0:
            resultado.append(i)
    return resultado

resultado_final = filtrar_pares([3, 4, 7, 10, 15, 20])
print(resultado_final)




### Mejora ###


def filtrar_pares(numeros):
    return [n for n in numeros if n % 2 == 0]

resultado_final = filtrar_pares([3, 4, 7, 10, 15, 20])
print(resultado_final)