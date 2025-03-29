import threading
import time

def tarea(numero):
    print(f"Hilo {numero} iniciado")
    time.sleep(2)
    print(f"Hilo {numero} terminado")

hilos = []

# Crear 5 hilos
for i in range(5):
    hilo = threading.Thread(target=tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado")