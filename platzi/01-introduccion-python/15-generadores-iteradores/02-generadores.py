# Ejemplo basico de generadores

def generador_simple():
    yield 1
    yield 2
    yield 3

gen = generador_simple()

print(next(gen))  # Salida: 1
print(next(gen))  # Salida: 2
print(next(gen))  # Salida: 3
# print(next(gen))  # Error: StopIteration



# generadores con bucles
def generar_pares(limite):
    for numero in range(2, limite + 1, 2):
        yield numero

for par in generar_pares(10):
    print(par)
# Salida:
# 2
# 4
# 6
# 8
# 10
