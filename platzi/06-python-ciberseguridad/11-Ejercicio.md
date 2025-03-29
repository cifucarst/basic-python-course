___

### **Código 

```python
import datetime

class DispositivoRed:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__registro_eventos = []

    def registrar_evento(self, mensaje):
        self.__registro_eventos.append(mensaje)

    def analizar_trafico(self):
        return f"{self.nombre}: Analizando tráfico de manera general"

    def ver_eventos(self):
        if self.__registro_eventos:
            print(f"Eventos registrados en {self.nombre}:")
            for evento in self.__registro_eventos:
                print(evento)
        else:
            print(f"No hay eventos registrados en {self.nombre}.")
        return ""

    def guardar_eventos(self):
        ahora = datetime.datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
        with open('registro_eventos.txt', 'a') as archivo:
            archivo.write(f"\n[{fecha_hora}] Eventos de {self.nombre}:\n")
            if self.__registro_eventos:
                for evento in self.__registro_eventos:
                    archivo.write(f"  - {evento}\n")
            else:
                archivo.write("  No hay eventos registrados.\n")


class Router(DispositivoRed):
    def analizar_trafico(self):
        mensaje = f"{self.nombre}: Redireccionando paquetes a la red correcta."
        self.registrar_evento("Redireccionamiento exitoso a 192.168.1.1")
        return mensaje


class Switch(DispositivoRed):
    def analizar_trafico(self):
        mensaje = f"{self.nombre}: Enviando tramas a los dispositivos adecuados."
        self.registrar_evento("Trama enviada a MAC: AA:BB:CC:DD:EE:FF")
        return mensaje


class Servidor(DispositivoRed):
    def analizar_trafico(self):
        mensaje = f"{self.nombre}: Procesando solicitudes de clientes."
        self.registrar_evento("Petición HTTP recibida en /login")
        return mensaje


# Crear instancias
router = Router("Router")
switch = Switch("Switch")
servidor = Servidor("Servidor")

dispositivos = [router, switch, servidor]

# Llamar a los métodos
for d in dispositivos:
    print(d.analizar_trafico())  # Ya registra eventos automáticamente
    d.ver_eventos()  # Muestra eventos sin imprimir "None"
    d.guardar_eventos()  # Guarda todos los eventos en un archivo
```

---

### **¿Qué mejora este código?**

✅ **Ahora se guardan TODOS los eventos, no solo el de `analizar_trafico()`.**  
✅ **Mejor formato en el archivo de logs**, con un encabezado por dispositivo.  
✅ **No se registran eventos duplicados**, ya que `guardar_eventos()` solo usa los eventos registrados previamente.

---
