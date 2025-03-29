____

Continuemos con **Programación Orientada a Objetos en Ciberseguridad**. 🔥

### **📌 Siguiente tema: Métodos Estáticos y de Clase**

Hasta ahora, hemos trabajado con **métodos de instancia**, que requieren que un objeto sea creado para ser utilizados. Ahora exploraremos dos tipos de métodos que no dependen de una instancia específica:

1. **Métodos estáticos (`@staticmethod`)**
    
    - No requieren acceso a los atributos del objeto (`self`).
    - Se usan cuando una función lógica pertenece a la clase pero no necesita modificar sus atributos.
    - Ejemplo en ciberseguridad: Conversión de direcciones IP.
2. **Métodos de clase (`@classmethod`)**
    
    - Reciben un argumento `cls`, que representa la clase en sí.
    - Se usan para modificar atributos de la clase en lugar de una instancia.
    - Ejemplo en ciberseguridad: Contar el número de dispositivos creados.

---

### **Ejemplo práctico**

Implementaremos una clase **"AnalizadorIP"** con: ✔ Un **método estático** para verificar si una IP es privada.  
✔ Un **método de clase** para contar cuántos objetos se han creado.

```python
import ipaddress

class AnalizadorIP:
    total_ips_analizadas = 0  # Atributo de clase
    
    def __init__(self, ip):
        self.ip = ip
        AnalizadorIP.total_ips_analizadas += 1  # Incrementamos el contador
    
    def analizar(self):
        return f"Analizando tráfico en la IP: {self.ip}"
    
    @staticmethod
    def es_ip_privada(ip):
        """Método estático para verificar si una IP es privada."""
        return ipaddress.ip_address(ip).is_private
    
    @classmethod
    def cantidad_ips_analizadas(cls):
        """Método de clase para contar cuántas IPs se han analizado."""
        return f"Total de IPs analizadas: {cls.total_ips_analizadas}"


# Ejemplo de uso
ip1 = AnalizadorIP("192.168.1.1")
ip2 = AnalizadorIP("8.8.8.8")

print(ip1.analizar())
print(ip2.analizar())

# Usamos el método estático sin instanciar la clase
print(AnalizadorIP.es_ip_privada("192.168.1.1"))  # True
print(AnalizadorIP.es_ip_privada("8.8.8.8"))  # False

# Usamos el método de clase
print(AnalizadorIP.cantidad_ips_analizadas())  # Total de IPs analizadas: 2
```

---

### **📌 Retos opcionales**

🔹 **Reto 1:** Añadir un método estático que valide si una dirección IP es válida.  
🔹 **Reto 2:** Modificar el método de clase para que también cuente direcciones IPv4 e IPv6 por separado.

📢 ¡Pruébalo y dime qué opinas! 🚀 ¿Quieres seguir con otro concepto o hacer los retos? 😃



Ejercicio realizado por mi

```python
import ipaddress
import re

  
class AnalizadorIP:

	total_ipsv4_analizadas = 0 # Atributo de clase
	total_ipsv6_analizadas = 0

  

def __init__(self, ip):
	self.ip = ip

	if AnalizadorIP.validar_ip(self.ip) == 1:
		AnalizadorIP.total_ipsv4_analizadas += 1 # Incrementamos el contador
	elif AnalizadorIP.validar_ip(self.ip) == 2:
		AnalizadorIP.total_ipsv6_analizadas += 1

	def analizar(self):
		return f"Analizando tráfico en la IP: {self.ip}"

	@staticmethod
	def es_ip_privada(ip):
	"""Método estático para verificar si una IP es privada."""
		return ipaddress.ip_address(ip).is_private

	@classmethod
	def cantidad_ips_analizadas(cls):
	"""Método de clase para contar cuántas IPs se han analizado."""
		return f"Total de IPSV4 analizadas: {cls.total_ipsv4_analizadas}\nTotal de IPSV6 analizadas: {cls.total_ipsv6_analizadas}"

	@staticmethod
	def validar_ip(ip):
		pattern1 = r"\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b"
		pattern2 = r"\b([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"

		if re.findall(pattern1, ip):
			return 1
		elif re.findall(pattern2, ip):
			return 2
		else:
			return False

  

# Ejemplo de uso

ip1 = AnalizadorIP("192.168.1.1")
ip2 = AnalizadorIP("8.8.8.8")
ip3 = AnalizadorIP("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
ip4 = AnalizadorIP("2001:0db8:85f3:0000:0000:8a2e:0370:7434")
ip5 = AnalizadorIP("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

print(ip1.analizar())
print(ip2.analizar())

# Usamos el método estático sin instanciar la clase

print(AnalizadorIP.es_ip_privada("192.168.1.1")) # True
print(AnalizadorIP.es_ip_privada("8.8.8.8")) # False


# Usamos el método de clase
print(AnalizadorIP.cantidad_ips_analizadas())
```

