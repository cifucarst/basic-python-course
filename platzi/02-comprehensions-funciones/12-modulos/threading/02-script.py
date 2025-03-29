import threading

def tarea():
    print("¡Hola desde un hilo!")

# Crear un hilo
hilo = threading.Thread(target=tarea)

# Iniciar el hilo
hilo.start()

# Esperar a que termine el hilo
hilo.join()

print("El hilo ha terminado")