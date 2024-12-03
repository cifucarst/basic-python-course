# Ejercicio 1: Suma de elementos

# Escribe un programa que calcule la suma de todos los elementos en una lista de números.


# def sum_elements(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total

# if __name__ == '__main__':
#     numbers = [10,2,3,4,5]
#     print(sum_elements(numbers))


# ////////////////////////////////////////////////////////////////////////////

# Otra version

def sum_elements(numbers):
    return sum(numbers)

if __name__ == '__main__':
    numbers = [10, 2, 3, 4, 5]
    print(sum_elements(numbers))