# 6. sys.stdin, sys.stdout y sys.stderr
# Estos objetos permiten interactuar con las entradas y salidas estándar.

# Ejemplo práctico: Redirigir salida estándar


import sys

# Redirigir la salida estándar a un archivo
with open("output.txt", "w") as f:
    sys.stdout = f
    print("Este mensaje se escribe en el archivo.")
    print("Y este también.")

# Restaurar la salida estándar
sys.stdout = sys.__stdout__
print("El mensaje se escribe en la terminal nuevamente.")