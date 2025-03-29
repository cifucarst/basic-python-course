x = 5

def modify_global():
    global x
    x += 3
    print(f"Valor modificado: {x}")

modify_global()
print(x)