x = "global"

def outer_function():
    x = "enclosing"

    # funcion interna
    def inner_function():
        x = "local" 
        print(x)
    
    inner_function()
    print(x)


outer_function()
print(x)