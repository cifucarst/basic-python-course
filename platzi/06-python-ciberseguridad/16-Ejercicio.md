___

¡Genial! Vamos con otro ejercicio desafiante en **POO y ciberseguridad**.

---

### **Ejercicio: Análisis de Logs de Acceso**

Vas a construir una clase `AnalizadorLogs` que simule el análisis de logs de acceso de un servidor.

#### **Requisitos:**

1. **Debe leer un archivo de log** (`accesos.log`), que tiene líneas con el formato:
    
    ```
    [2025-02-15 14:32:10] - usuario: admin, IP: 192.168.1.10, acceso: exitoso
    [2025-02-15 14:35:25] - usuario: hacker, IP: 203.0.113.5, acceso: fallido
    ```
    
2. **Debe contar los accesos exitosos y fallidos.**
    
3. **Debe identificar las IPs sospechosas** (IPs con 3 o más intentos fallidos).
    
4. **Debe permitir filtrar los accesos por un usuario específico.**
    
5. **Debe imprimir un resumen del análisis.**
    

---

### **Ejemplo de salida esperada:**

```
Total accesos exitosos: 15
Total accesos fallidos: 8
IPs sospechosas (más de 3 intentos fallidos): 
- 203.0.113.5 (4 intentos fallidos)
- 45.67.89.10 (5 intentos fallidos)

Accesos del usuario 'admin':
- [2025-02-15 14:32:10] - usuario: admin, IP: 192.168.1.10, acceso: exitoso
- [2025-02-15 15:00:10] - usuario: admin, IP: 192.168.1.11, acceso: fallido
```

---

### **Pistas:**

🔹 Usa expresiones regulares (`re`) para extraer usuario, IP y estado del acceso.  
🔹 Usa un diccionario para contar intentos fallidos por IP.  
🔹 Carga el archivo con `open("accesos.log")` y procesa cada línea.

¡A ver cómo lo resuelves! 🚀 Cuando tengas tu solución, compártela y la revisamos juntos. 💡


```
import re

class AnalizadorLogs:
	accesos_exitosos = 0
	accesos_fallidos = 0
	intentos_fallidos = {}

	def __init__(self):
		AnalizadorLogs.contar_accessos()

	@staticmethod
	def contar_accessos():
		with open('access.log', 'r') as archivo:
			for linea in archivo:
				if 'exitoso' in linea:
					AnalizadorLogs.accesos_exitosos += 1
				elif 'fallido' in linea:
					AnalizadorLogs.accesos_fallidos += 1
					ip = AnalizadorLogs.identificar_ip_en_linea(linea)
					if ip:
						if ip in AnalizadorLogs.intentos_fallidos:
							AnalizadorLogs.intentos_fallidos[ip] += 1
				else:
					AnalizadorLogs.intentos_fallidos[ip] = 1

	@staticmethod
	def identificar_ip_en_linea(linea):
		ips = re.findall(r"\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b", linea)
		if ips:
			return ips[0]
		return None

  

	def identificar_ip_sospechosas(self):
		sospechosas = {}
		for ip, intentos in AnalizadorLogs.intentos_fallidos.items():
			if intentos >= 3:
				sospechosas[ip] = intentos

		return sospechosas

  
	@staticmethod
	def filtrar_por_usuario(nombre_usuario):
		accesos_usuario = []
		with open('access.log', 'r') as archivo:
			for linea in archivo:
				if nombre_usuario in linea:
					accesos_usuario.append(linea.strip())

		return accesos_usuario

  

	def resumen_analisis(self):
		print(f"Total accesos exitosos: {AnalizadorLogs.accesos_exitosos}")
		print(f"Total accesos fallidos: {AnalizadorLogs.accesos_fallidos}")
		sospechosas = self.identificar_ip_sospechosas()
		if sospechosas:
			print("IPs sospechosas (más de 3 intentos fallidos):")
			for ip, intentos in sospechosas.items():
				print(f"- {ip} ({intentos} intentos fallidos)")

  

# Ejemplo de uso
analizador = AnalizadorLogs()
analizador.resumen_analisis()

accesos_admin = AnalizadorLogs.filtrar_por_usuario('admin')
if accesos_admin:
	print("\nAccesos del usuario 'admin':")
	for acceso in accesos_admin:
		print(f"- {acceso}")
```