# Ejemplos practicos

# Calcular la suma de numeros en un rango
suma = 0

for i in range(1, 11):  # Números del 1 al 10
    suma += i

print("La suma es:", suma)
# Salida: La suma es: 55



# Buscar un elemento en una lista
elementos = ["a", "b", "c", "d"]
buscar = "c"

for elemento in elementos:
    if elemento == buscar:
        print(f"Encontrado: {buscar}")
        break
else:
    print(f"No se encontró: {buscar}")
# Salida: Encontrado: c



# validar entrada del usuario
while True:
    entrada = input("Escribe un número entre 1 y 10: ")
    if entrada.isdigit() and 1 <= int(entrada) <= 10:
        print(f"Correcto: {entrada}")
        break
    else:
        print("Número inválido, inténtalo de nuevo.")
