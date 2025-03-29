import threading

def imprimir_mensaje(mensaje):
    print(f"Mensaje: {mensaje}")

# Crear un hilo con argumentos
hilo = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo",))

hilo.start()
hilo.join()