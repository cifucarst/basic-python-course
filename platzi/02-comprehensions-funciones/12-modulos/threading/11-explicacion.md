¡Genial! Vamos a hacer un ejercicio práctico con `threading` aplicado a ciberseguridad. Crearemos un **escáner de puertos concurrente** en Python. La idea es que el programa escanee múltiples puertos de un objetivo al mismo tiempo usando hilos, lo que acelerará el escaneo en comparación con un enfoque secuencial.

---

## **🛠 Ejercicio: Escáner de Puertos con `threading`**
Este script utilizará `socket` para intentar conectarse a diferentes puertos y `threading` para hacer múltiples intentos en paralelo.

### **Código del escáner de puertos**
```python
import threading
import socket

# Función para escanear un solo puerto
def escanear_puerto(ip, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Tiempo máximo de espera para la conexión
        resultado = sock.connect_ex((ip, puerto))  # 0 significa que el puerto está abierto
        if resultado == 0:
            print(f"[+] Puerto {puerto} abierto")

# Función principal que lanza hilos para escanear múltiples puertos
def escaner(ip, puertos):
    hilos = []
    
    for puerto in puertos:
        hilo = threading.Thread(target=escanear_puerto, args=(ip, puerto))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

# Parámetros del escaneo
objetivo = "scanme.nmap.org"  # Puedes cambiarlo por una IP específica
rango_puertos = range(1, 1025)  # Escanea los primeros 1024 puertos

print(f"Iniciando escaneo en {objetivo}...\n")
escaner(objetivo, rango_puertos)
print("\nEscaneo finalizado.")
```

---

## **🔍 Explicación del código**
1. **`escanear_puerto(ip, puerto)`**: Intenta conectarse a un puerto. Si la conexión es exitosa, imprime que el puerto está abierto.
2. **`escaner(ip, puertos)`**: Crea múltiples hilos para escanear varios puertos en paralelo.
3. **`socket.connect_ex((ip, puerto))`**: Devuelve `0` si el puerto está abierto, otro valor si está cerrado.
4. **`threading.Thread(target=escanear_puerto, args=(ip, puerto))`**: Crea un hilo por cada puerto.
5. **`hilo.start()` y `hilo.join()`**: Inicia y espera que todos los hilos terminen antes de continuar.

---

## **💡 ¿Cómo mejorarlo?**
- **Usar `Queue`** para manejar mejor los hilos y evitar crear demasiados.
- **Soporte para escaneo de rangos personalizados**.
- **Opciones de escaneo más avanzadas (e.g., detección de servicios con `banner grabbing`)**.

🚀 **¿Te gustaría mejorar este escáner o agregarle más funcionalidades, como detección de servicios?**