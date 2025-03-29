import threading

class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        print(f"Hilo en ejecución: {self.nombre}")

# Crear e iniciar un hilo
hilo = MiHilo("Hilo 1")
hilo.start()
hilo.join()