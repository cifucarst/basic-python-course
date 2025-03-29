import multiprocessing
import time

def worker(name):
    print(f"Proceso {name} iniciado.")
    time.sleep(2)
    print(f"Proceso {name} finalizado.")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("A",))
    p2 = multiprocessing.Process(target=worker, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Todos los procesos han terminado.")