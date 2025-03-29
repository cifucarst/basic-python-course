# platzi closures y scope

x = 100

def local_function():
    x = 10 # Variable local
    print(f"El valor de la variables: {x}")


def show_global():
    print(f"El valor de la variable global es {x}")

local_function()
print(x)