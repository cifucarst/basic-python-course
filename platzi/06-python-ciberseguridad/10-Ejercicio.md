___


### **Código

```python
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


class Router(DispositivoRed):
    def analizar_trafico(self):
        mensaje = f"{self.nombre}: Redireccionando paquetes a la red correcta."
        self.registrar_evento("- Redireccionamiento exitoso a 192.168.1.1")
        return mensaje


class Switch(DispositivoRed):
    def analizar_trafico(self):
        mensaje = f"{self.nombre}: Enviando tramas a los dispositivos adecuados."
        self.registrar_evento("- Trama enviada a MAC: AA:BB:CC:DD:EE:FF")
        return mensaje


class Servidor(DispositivoRed):
    def analizar_trafico(self):
        mensaje = f"{self.nombre}: Procesando solicitudes de clientes."
        self.registrar_evento("- Petición HTTP recibida en /login")
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
```

---

### **🔍 Mejoras clave**

✅ **Encapsulamiento correcto** de `__registro_eventos`.  
✅ **Cada dispositivo registra eventos automáticamente** en `analizar_trafico()`.  
✅ **Evita que aparezca `None`** al llamar `ver_eventos()`.

---

📌 **Próximo reto (Opcional)**:  
📢 _Agrega un método `guardar_eventos()` en `DispositivoRed` para escribir los eventos en un archivo de texto._  
Así el administrador podría revisarlos más tarde. 🚀

¿Qué opinas de estos cambios? ¿Quieres seguir explorando más conceptos en POO? 😊