# 2. sys.exit()
# Permite salir del programa con un código de estado. Por convención, un código 0 indica que el programa terminó correctamente; cualquier otro valor señala un error.

# Ejemplo práctico: Terminar el programa si no se cumplen condiciones


import sys

user_input = input("Escribe 'salir' para terminar: ")
if user_input.lower() == 'salir':
    print("¡Adiós!")
    sys.exit(0)

print("No escribiste 'salir', el programa continúa.")
