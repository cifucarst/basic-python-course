import threading
import queue

cola = queue.Queue()

def productor():
    for i in range(5):
        cola.put(i)
        print(f"Producido: {i}")

def consumidor():
    while not cola.empty():
        item = cola.get()
        print(f"Consumido: {item}")

hilo1 = threading.Thread(target=productor)
hilo2 = threading.Thread(target=consumidor)

hilo1.start()
hilo1.join()  # Espera a que el productor termine antes de consumir
hilo2.start()
hilo2.join()