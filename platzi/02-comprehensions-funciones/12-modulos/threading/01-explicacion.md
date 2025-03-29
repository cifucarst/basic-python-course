## **Guía Completa de la Librería `threading` en Python**

La librería `threading` en Python permite la ejecución de múltiples hilos (*threads*) en paralelo dentro de un mismo proceso. Es útil cuando queremos realizar tareas concurrentes sin necesidad de crear procesos separados, lo que ahorra memoria y facilita la comunicación entre hilos.

---

# **1. ¿Qué es un hilo (thread) en Python?**
Un **hilo** es una unidad de ejecución más pequeña dentro de un proceso. Cada proceso en un sistema operativo puede contener múltiples hilos que comparten la misma memoria.

Python admite **multihilos** (*multithreading*), pero debido al **GIL (Global Interpreter Lock)**, no se obtiene una ejecución paralela real en tareas intensivas en CPU. Sin embargo, sí es útil en tareas de I/O, como manejo de archivos, redes, o interfaces gráficas.

---

# **2. Creación y manejo de hilos en Python**
Python proporciona la librería `threading` para trabajar con hilos. Veamos cómo crear y manejar hilos.

## **Ejemplo básico de un hilo**
```python
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
```
### **Explicación**
- `Thread(target=tarea)`: Crea un hilo que ejecuta la función `tarea`.
- `start()`: Inicia la ejecución del hilo.
- `join()`: Espera a que el hilo termine antes de continuar con el código principal.

---

# **3. Pasar argumentos a un hilo**
Podemos pasar argumentos a la función ejecutada por un hilo usando `args`.

```python
import threading

def imprimir_mensaje(mensaje):
    print(f"Mensaje: {mensaje}")

# Crear un hilo con argumentos
hilo = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo",))

hilo.start()
hilo.join()
```

### **Nota**: 
- `args` recibe una tupla. Si hay un solo argumento, se debe poner una coma: `args=("Hola",)`

---

# **4. Crear hilos con clases**
También podemos definir hilos mediante clases heredando `threading.Thread`.

```python
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
```

### **Explicación**
- Sobreescribimos `run()`, que es la función que se ejecuta cuando se inicia el hilo con `start()`.

---

# **5. Manejo de hilos múltiples**
Podemos ejecutar múltiples hilos simultáneamente.

```python
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
```

---

# **6. Sincronización de hilos con `Lock`**
Cuando varios hilos acceden a una misma variable compartida, pueden ocurrir condiciones de carrera (*race conditions*). Para evitarlo, usamos `Lock`.

```python
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
```

### **Explicación**
- `with lock:` asegura que solo un hilo modifique `contador` a la vez, evitando problemas de concurrencia.

---

# **7. Uso de `Queue` para comunicación entre hilos**
Cuando varios hilos deben compartir información de manera segura, usamos `queue.Queue`.

```python
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
```

---

# **8. Aplicaciones del multithreading en la vida real**
El uso de `threading` es útil en situaciones como:
1. **Interfaces Gráficas (GUI)**: Para que la interfaz no se congele mientras se ejecutan tareas en segundo plano.
2. **Manejo de sockets y servidores web**: Para atender múltiples clientes al mismo tiempo.
3. **Procesamiento de archivos grandes**: Para leer y escribir en paralelo.
4. **Web Scraping**: Para hacer múltiples solicitudes HTTP de manera concurrente.

### **Ejemplo: Descarga de archivos en paralelo**
```python
import threading
import requests

urls = [
    "https://www.example.com/file1.jpg",
    "https://www.example.com/file2.jpg"
]

def descargar(url):
    response = requests.get(url)
    print(f"Descargado {url}, tamaño: {len(response.content)} bytes")

hilos = []
for url in urls:
    hilo = threading.Thread(target=descargar, args=(url,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todas las descargas han finalizado.")
```
---

# **9. Limitaciones de `threading` y alternativas**
- **El GIL (Global Interpreter Lock)** impide que varios hilos ejecuten código Python al mismo tiempo. `threading` es ideal para tareas I/O, pero no para tareas intensivas en CPU.
- Para cómputo paralelo real, usa `multiprocessing`, que crea procesos en lugar de hilos.

### **Ejemplo con `multiprocessing`**
```python
import multiprocessing

def tarea(numero):
    print(f"Proceso {numero} en ejecución")

procesos = [multiprocessing.Process(target=tarea, args=(i,)) for i in range(5)]

for proceso in procesos:
    proceso.start()

for proceso in procesos:
    proceso.join()
```

---

# **10. Conclusión**
- `threading` permite ejecutar múltiples tareas simultáneamente en un mismo proceso.
- Es útil para tareas I/O como lectura de archivos, descarga de datos y redes.
- Se debe manejar correctamente con `Lock` para evitar problemas de concurrencia.
- Para tareas intensivas en CPU, `multiprocessing` es una mejor alternativa.

¿Quieres que hagamos un ejercicio práctico con `threading` aplicado a ciberseguridad? 🚀