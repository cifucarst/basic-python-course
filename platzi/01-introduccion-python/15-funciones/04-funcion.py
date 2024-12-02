# decoradores
def decorador_saludo(funcion):
    def envoltura():
        print("¡Hola!")
        funcion()
        print("¡Adiós!")
    return envoltura

@decorador_saludo
def presentacion():
    print("Soy un decorador.")

presentacion()
# Salida:
# ¡Hola!
# Soy un decorador.
# ¡Adiós!
