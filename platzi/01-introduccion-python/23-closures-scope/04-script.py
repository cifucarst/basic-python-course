def outer_function():
    x = "enclosing"
    def inner_function():
        nonlocal x
        x = 'modified'
        print(f"El valor en inner es: {x}")
    inner_function()
    print(f"El valor outer: {x}")

    
outer_function()