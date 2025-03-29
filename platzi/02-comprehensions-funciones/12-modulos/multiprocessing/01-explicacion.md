La librería `multiprocessing` de Python permite ejecutar tareas en paralelo utilizando múltiples procesos. A diferencia de `threading`, que maneja múltiples hilos en un solo proceso (afectado por el Global Interpreter Lock, GIL), `multiprocessing` permite ejecutar procesos independientes, aprovechando mejor los núcleos de la CPU.

---

## 🔹 Conceptos clave de `multiprocessing`
1. **Procesos**: Cada proceso tiene su propio espacio de memoria y ejecuta su propia instancia de Python.
2. **Colas y Pipes**: Permiten la comunicación entre procesos.
3. **Pools de procesos**: Facilitan la ejecución de múltiples tareas en paralelo sin gestionar manualmente los procesos.
4. **Bloqueos (Locks)**: Sincronizan procesos para evitar condiciones de carrera.

---

## 1️⃣ **Ejemplo básico: Crear y ejecutar procesos**
Aquí creamos dos procesos independientes.

```python
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
```
🔹 `start()` inicia el proceso.  
🔹 `join()` espera a que termine antes de continuar.

📌 **Salida esperada:**
```
Proceso A iniciado.
Proceso B iniciado.
Proceso A finalizado.
Proceso B finalizado.
Todos los procesos han terminado.
```

---

## 2️⃣ **Ejemplo con `Pool`: Procesamiento paralelo de una lista**
Aquí aplicamos una función a múltiples elementos en paralelo.

```python
import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(square, numbers)
    
    print(f"Resultados: {results}")
```

🔹 `Pool(processes=3)`: Usa hasta 3 procesos simultáneamente.  
🔹 `map(square, numbers)`: Aplica la función `square` en paralelo.  

📌 **Salida esperada:**
```
Resultados: [1, 4, 9, 16, 25]
```

---

## 🚀 **Ejemplo en ciberseguridad: Escaneo de puertos en paralelo**
Podemos usar `multiprocessing` para acelerar un escaneo de puertos.

```python
import multiprocessing
import socket

def scan_port(target_ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[*] Puerto {port} abierto")

if __name__ == "__main__":
    target = "scanme.nmap.org"  # Prueba con un host accesible
    ports = range(1, 1025)

    with multiprocessing.Pool(processes=10) as pool:
        pool.starmap(scan_port, [(target, port) for port in ports])
```

🔹 `starmap(scan_port, [(target, port) for port in ports])`: Permite pasar múltiples argumentos a la función.  
🔹 `socket.connect_ex((target_ip, port))`: Verifica si el puerto está abierto.  
🔹 `settimeout(1)`: Evita que el escaneo se bloquee en puertos cerrados.  

📌 **Salida esperada:**
```
[*] Puerto 22 abierto
[*] Puerto 80 abierto
...
```

---

## 4️⃣ **Ejemplo con colas: Gestión de tareas**
Usamos `Queue` para distribuir tareas a múltiples procesos.

```python
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
```

🔹 `Queue.get()`: Extrae un elemento de la cola.  
🔹 `Queue.put()`: Agrega un elemento a la cola.  

📌 **Salida esperada:**
```
Procesando: Tarea 0
Procesando: Tarea 1
Finalizado: Tarea 0
Finalizado: Tarea 1
...
Todas las tareas han sido procesadas.
```

---

## 🔥 **Ejemplo en ciberseguridad: Ataque de fuerza bruta en paralelo**
Este ejemplo intenta adivinar contraseñas de un hash SHA256 en paralelo.

```python
import multiprocessing
import hashlib

def crack_hash(password):
    hash_obj = hashlib.sha256(password.encode())
    hashed_password = hash_obj.hexdigest()
    
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd60492f1788b2df8c6"  # hash de "password"
    
    if hashed_password == target_hash:
        print(f"[+] Contraseña encontrada: {password}")
        return True
    return False

if __name__ == "__main__":
    wordlist = ["123456", "qwerty", "password", "admin", "welcome"]
    
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(crack_hash, wordlist)

    if any(results):
        print("Ataque exitoso.")
    else:
        print("No se encontró la contraseña.")
```

🔹 `hashlib.sha256(password.encode()).hexdigest()`: Calcula el hash SHA-256 de la contraseña.  
🔹 `pool.map(crack_hash, wordlist)`: Prueba cada palabra en paralelo.  

📌 **Salida esperada:**
```
[+] Contraseña encontrada: password
Ataque exitoso.
```

---

## 🔹 **Conclusión**
La librería `multiprocessing` es fundamental para aprovechar mejor la CPU en tareas pesadas. En ciberseguridad, se usa para:
✅ Escaneos de puertos más rápidos  
✅ Ataques de fuerza bruta más eficientes  
✅ Procesamiento de grandes volúmenes de datos  

📌 **¿Te gustaría que implemente otro ejemplo más avanzado?** 🚀