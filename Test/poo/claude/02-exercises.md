# Ejercicios de POO en Python para Ciberseguridad

## **EJERCICIOS BÁSICOS (1-5)**

### Ejercicio 1: Clase Usuario Básica
Crea una clase `Usuario` con los siguientes atributos:
- `nombre` (string)
- `email` (string) 
- `contraseña` (string, privada)
- `activo` (boolean, por defecto True)

Implementa métodos para:
- `cambiar_contraseña(nueva_contraseña)`: cambia la contraseña
- `desactivar_usuario()`: cambia el estado a inactivo
- `mostrar_info()`: muestra nombre, email y estado (sin mostrar contraseña)

### Ejercicio 2: Validador de Contraseñas
Crea una clase `ValidadorContraseña` que tenga un método estático `es_segura(contraseña)` que verifique:
- Mínimo 8 caracteres
- Al menos una letra mayúscula
- Al menos una letra minúscula  
- Al menos un número
- Al menos un carácter especial (!@#$%^&*)

El método debe retornar `True` si cumple todos los criterios, `False` en caso contrario.

### Ejercicio 3: Log de Eventos de Seguridad
Crea una clase `LogSeguridad` que permita registrar eventos de seguridad:
- Atributo `eventos` (lista privada)
- Método `registrar_evento(tipo, descripcion, timestamp=None)`: si no se pasa timestamp, usar datetime.now()
- Método `obtener_eventos()`: retorna todos los eventos
- Método `filtrar_por_tipo(tipo)`: retorna eventos de un tipo específico

### Ejercicio 4: Dirección IP
Crea una clase `DireccionIP` que:
- Reciba una IP como string en el constructor
- Valide que sea una IPv4 válida (formato xxx.xxx.xxx.xxx donde xxx es 0-255)
- Tenga métodos para determinar si es:
  - IP privada (rangos: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
  - IP de loopback (127.0.0.0/8)
- Método `__str__()` que retorne la IP formateada

### Ejercicio 5: Hash Simple
Crea una clase `GeneradorHash` que:
- Tenga métodos estáticos para generar hashes MD5, SHA1 y SHA256 de un texto
- Método `comparar_hash(texto, hash_esperado, algoritmo)`: compare si el hash del texto coincide
- Método `generar_todos(texto)`: retorne un diccionario con los tres tipos de hash

---

## **EJERCICIOS INTERMEDIOS (6-10)**

### Ejercicio 6: Sistema de Autenticación con Herencia
Crea una clase base `SistemaAuth` y dos clases derivadas:

**Clase base `SistemaAuth`:**
- Atributos: `usuarios` (diccionario), `intentos_fallidos` (diccionario)
- Método abstracto `autenticar(usuario, credencial)`
- Método `bloquear_usuario(usuario)` si supera 3 intentos fallidos
- Método `esta_bloqueado(usuario)`

**Clases derivadas:**
- `AuthContraseña`: autentica con usuario/contraseña
- `AuthToken`: autentica con token JWT (simulado con string)

### Ejercicio 7: Escáner de Puertos Básico
Crea una clase `EscanerPuertos` que:
- Reciba una IP objetivo en el constructor
- Tenga método `escanear_puerto(puerto)`: simula escaneo retornando "abierto", "cerrado" o "filtrado" aleatoriamente
- Método `escanear_rango(puerto_inicio, puerto_fin)`: escanea un rango y retorna diccionario
- Método `puertos_comunes()`: escanea puertos 21, 22, 23, 25, 53, 80, 110, 443, 993, 995
- Implemente logging de todas las operaciones

### Ejercicio 8: Analizador de Headers HTTP
Crea una clase `AnalizadorHeaders` que:
- Reciba un diccionario de headers HTTP en el constructor
- Método `verificar_seguridad()`: verifique presencia de headers de seguridad importantes:
  - Content-Security-Policy
  - X-Frame-Options  
  - X-XSS-Protection
  - Strict-Transport-Security
- Método `generar_reporte()`: retorna dict con headers presentes/ausentes y recomendaciones
- Método `es_vulnerable()`: determina si faltan headers críticos

### Ejercicio 9: Detector de Anomalías de Red
Crea una clase `DetectorAnomalias` que:
- Mantenga estadísticas de tráfico normal (IPs, puertos, protocolos)
- Método `entrenar(datos_trafico)`: recibe lista de tuplas (ip_origen, puerto_destino, protocolo)
- Método `detectar_anomalia(conexion)`: determina si una conexión es anómala
- Método `obtener_estadisticas()`: retorna stats del tráfico normal
- Use conceptos estadísticos básicos (frecuencia, percentiles)

### Ejercicio 10: Gestor de Certificados SSL
Crea una clase `GestorCertificados` que:
- Almacene información de certificados SSL (dominio, fecha_emision, fecha_expiracion, emisor)
- Método `agregar_certificado(dominio, dias_validez, emisor)`
- Método `verificar_expiracion()`: retorna certificados que expiran en menos de 30 días
- Método `renovar_certificado(dominio, nuevos_dias_validez)`
- Método `generar_alerta(dominio)`: crea alerta para certificados próximos a expirar

---

## **EJERCICIOS AVANZADOS (11-15)**

### Ejercicio 11: Framework de Análisis de Malware
Diseña un sistema con múltiples clases:

**Clase `Muestra`:**
- Atributos: hash, tamaño, tipo_archivo, fecha_analisis
- Método `calcular_hash()`

**Clase `AnalizadorEstatico`:**
- Método `analizar_strings(muestra)`: extrae strings sospechosos
- Método `analizar_imports(muestra)`: analiza imports peligrosos
- Método `calcular_entropia(muestra)`: calcula entropía del archivo

**Clase `AnalizadorComportamental`:**
- Método `simular_ejecucion(muestra)`: simula análisis dinámico
- Método `detectar_comportamientos()`: identifica comportamientos maliciosos

**Clase `GeneradorReporte`:**
- Consolida análisis y genera reporte final con scoring de riesgo

### Ejercicio 12: Sistema de Correlación de Eventos SIEM
Implementa un mini-SIEM con:

**Clase `Evento`:**
- timestamp, source_ip, event_type, severity, description

**Clase `ReglaCorrelacion`:** (clase abstracta)
- Método abstracto `evaluar(eventos)`

**Clases derivadas de reglas:**
- `ReglaRateLimiting`: detecta muchos eventos del mismo IP
- `ReglaPatronTemporal`: detecta secuencias específicas de eventos
- `ReglaGeolocalizacion`: detecta accesos desde ubicaciones anómalas

**Clase `MotorCorrelacion`:**
- Gestiona reglas y evalúa eventos
- Genera alertas cuando se activan reglas

### Ejercicio 13: Honeypot Simulado con Decoradores
Crea un sistema de honeypot usando decoradores y POO:

**Decorador `@log_intento_acceso`:**
- Registra todos los intentos de acceso

**Decorador `@detectar_ataques`:**
- Identifica patrones de ataque (fuerza bruta, inyección SQL, etc.)

**Clase `ServicioHoneypot`:** (clase abstracta)
- Métodos que simulan servicios (SSH, FTP, HTTP)

**Clases derivadas:**
- `SSHHoneypot`, `FTPHoneypot`, `HTTPHoneypot`
- Cada una implementa respuestas específicas a intentos de ataque

### Ejercicio 14: Sistema de Gestión de Vulnerabilidades
Implementa un sistema complejo de gestión:

**Clase `Vulnerabilidad`:**
- CVE, CVSS score, descripción, fecha_descubrimiento, estado

**Clase `Activo`:**
- IP, hostname, servicios, vulnerabilidades asociadas

**Clase `EscanerVulnerabilidades`:** (usando patrón Strategy)
- Diferentes estrategias de escaneo (Nessus, OpenVAS, manual)

**Clase `GestorVulnerabilidades`:**
- CRUD de vulnerabilidades y activos
- Priorización basada en CVSS y criticidad del activo
- Generación de reportes ejecutivos y técnicos
- Tracking de remediación

### Ejercicio 15: Simulador de Red con Ataques
Crea un simulador avanzado:

**Clase `Nodo`:** (clase abstracta)
- Representa dispositivos de red

**Clases derivadas:**
- `Servidor`, `Cliente`, `Router`, `Firewall`
- Cada uno con comportamientos específicos

**Clase `Red`:**
- Gestiona topología de red
- Simula propagación de tráfico

**Clase `Atacante`:**
- Implementa diferentes tipos de ataques (DDoS, MitM, Port Scanning)
- Usa patrón Command para ejecutar ataques

**Clase `IDS`:**
- Detecta patrones de ataque
- Genera alertas y contramedidas

**Clase `SimuladorSeguridad`:**
- Orquesta toda la simulación
- Permite configurar escenarios de ataque/defensa

---

## **Instrucciones para el Estudiante**

1. **Resuelve los ejercicios en orden** - cada nivel construye sobre el anterior
2. **Enfócate en buenas prácticas de POO:**
   - Encapsulación (atributos privados cuando sea necesario)
   - Herencia (reutilización de código)
   - Polimorfismo (métodos que se comportan diferente según la clase)
   - Abstracción (interfaces claras)

3. **Considera aspectos de seguridad:**
   - Validación de entrada
   - Manejo de errores
   - Logging de eventos de seguridad
   - Principio de menor privilegio

4. **Documenta tu código** con docstrings y comentarios

5. **Incluye manejo de excepciones** apropiado para cada ejercicio

## **Formato de Entrega**
Para cada ejercicio, proporciona:
- Código completo
- Ejemplo de uso
- Breve explicación de las decisiones de diseño tomadas