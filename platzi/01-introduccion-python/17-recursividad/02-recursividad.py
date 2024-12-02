# Recursividad con ejemplos prácticos
# Potencia de un número

def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    return base * potencia(base, exponente - 1)  # Caso recursivo

print(potencia(2, 3))  # Salida: 8



# Suma de una lista
def suma_lista(lista):
    if len(lista) == 0:  # Caso base
        return 0
    return lista[0] + suma_lista(lista[1:])  # Caso recursivo

print(suma_lista([1, 2, 3, 4]))  # Salida: 10



# Invertir una cadena
def invertir_cadena(cadena):
    if len(cadena) == 0:  # Caso base
        return ""
    return cadena[-1] + invertir_cadena(cadena[:-1])  # Caso recursivo

print(invertir_cadena("Python"))  # Salida: nohtyP
