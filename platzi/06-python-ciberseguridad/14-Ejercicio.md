___

¡Genial! Sigamos practicando con un nuevo ejercicio de POO aplicado a ciberseguridad.

---

## **Ejercicio: Sistema de Registro de Intentos de Acceso**

Imagina que estás desarrollando un sistema para monitorear intentos de acceso a un servidor. Cada intento de acceso puede ser exitoso o fallido, y queremos registrar información relevante sobre ellos.

Tu tarea es crear una clase `RegistroAcceso` con los siguientes requisitos:

### **Requisitos:**

1. **Atributos de instancia:**
    
    - `usuario`: nombre del usuario que intenta acceder.
    - `direccion_ip`: dirección IP desde la que se intenta acceder.
    - `exitoso`: booleano (`True` si el intento fue exitoso, `False` si falló).
    - `timestamp`: momento en que ocurrió el intento (puedes usar `datetime.datetime.now()`).
2. **Atributos de clase:**
    
    - `total_intentos`: número total de intentos registrados.
    - `intentos_exitosos`: número de accesos exitosos.
    - `intentos_fallidos`: número de accesos fallidos.
3. **Métodos:**
    
    - `registrar_intento()`: Incrementa los contadores de intentos según si fue exitoso o fallido.
    - `ver_estadisticas()`: Método de clase que devuelve el número total de intentos, exitosos y fallidos.
    - `__str__()`: Representación en cadena del intento, indicando si fue exitoso o fallido.

---

### **Ejemplo de uso esperado:**

```python
intento1 = RegistroAcceso("admin", "192.168.1.10", True)
intento2 = RegistroAcceso("usuario1", "8.8.8.8", False)
intento3 = RegistroAcceso("hacker", "203.0.113.5", False)

print(intento1)
print(intento2)
print(intento3)

print(RegistroAcceso.ver_estadisticas())
```

💡 **Objetivo:** Practicar instancias, atributos de clase, `@classmethod` y `__str__`.

🔍 **Desafío extra:** Agregar un método que guarde los intentos en un archivo de texto.

---

🔥 ¡Inténtalo! Cuando tengas una solución, compártela aquí y te daré feedback. 😃

solucion que realice

```
from datetime import datetime

class RegistroAcceso:
	total_intentos = 0
	intentos_exitosos = 0
	intentos_fallidos = 0

	def __init__(self, nombre, direccion_ip, exitoso):
		self.nombre = nombre
		self.direccion_ip = direccion_ip
		self.exitoso = exitoso
		RegistroAcceso.total_intentos += 1
		self.registrar_intento()

  
	def registrar_intento(self):
		if self.exitoso:
			RegistroAcceso.intentos_exitosos += 1
		else:
			RegistroAcceso.intentos_fallidos += 1

  

	@staticmethod
	def ver_estadisticas():
		return f"Total intentos exitosos: {RegistroAcceso.intentos_exitosos}\nTotal intentos fallidos: {RegistroAcceso.intentos_fallidos}"

  

	def __str__(self):
		return f"[{datetime.now()}] - {self.nombre} con {self.direccion_ip} accedio al sistema con exito? {'si' if self.exitoso else 'no'}"

  

intento1 = RegistroAcceso("admin", "192.168.1.10", True)
intento2 = RegistroAcceso("usuario1", "8.8.8.8", False)
intento3 = RegistroAcceso("hacker", "203.0.113.5", False)

print(intento1)
print(intento2)
print(intento3)

print(RegistroAcceso.ver_estadisticas())
```