import threading

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(1000000):
        with lock:  # Bloquea la sección crítica
            contador += 1

hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=incrementar)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Valor final del contador: {contador}")