# Lista normal
numeros = [1, 2, 3, 4]

# Crear un iterador a partir de la lista
iterador = iter(numeros)

# Obtener los elementos uno a uno
print(next(iterador))  # Salida: 1
print(next(iterador))  # Salida: 2
print(next(iterador))  # Salida: 3
print(next(iterador))  # Salida: 4

# Intentar avanzar más allá de los elementos genera StopIteration
# print(next(iterador))  # Error: StopIteration



# iteradores personalizados
class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual > self.fin:
            raise StopIteration
        else:
            numero = self.actual
            self.actual += 1
            return numero

# Usar el iterador
contador = Contador(1, 5)

for numero in contador:
    print(numero)
# Salida:
# 1
# 2
# 3
# 4
# 5
