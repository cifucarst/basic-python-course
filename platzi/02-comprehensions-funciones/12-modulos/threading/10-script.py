import multiprocessing

def tarea(numero):
    print(f"Proceso {numero} en ejecución")

procesos = [multiprocessing.Process(target=tarea, args=(i,)) for i in range(5)]

for proceso in procesos:
    proceso.start()

for proceso in procesos:
    proceso.join()