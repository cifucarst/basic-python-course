import multiprocessing
import time

def worker(queue):
    while not queue.empty():
        task = queue.get()
        print(f"Procesando: {task}")
        time.sleep(1)
        print(f"Finalizado: {task}")

if __name__ == "__main__":
    task_queue = multiprocessing.Queue()

    for i in range(5):
        task_queue.put(f"Tarea {i}")

    processes = [multiprocessing.Process(target=worker, args=(task_queue,)) for _ in range(2)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Todas las tareas han sido procesadas.")