Te explico el módulo socket de Python de forma detallada, empezando por los conceptos básicos de redes que necesitas entender.

## Fundamentos de Redes

### ¿Qué es un Socket?
Un socket es como un "punto de conexión" entre dos programas que se comunican a través de una red. Imagínalo como un teléfono: necesitas un número (dirección IP + puerto) para llamar y alguien debe contestar del otro lado.

### Conceptos Clave de Redes

**Dirección IP**: Es como la dirección de una casa. Identifica de manera única un dispositivo en la red.
- IPv4: `192.168.1.100`
- IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Localhost: `127.0.0.1` (tu propia máquina)

**Puerto**: Es como el número de apartamento. Una misma IP puede tener múltiples servicios corriendo en diferentes puertos.
- Puerto 80: HTTP (páginas web)
- Puerto 443: HTTPS (páginas web seguras)
- Puerto 22: SSH
- Puertos 1024-65535: disponibles para aplicaciones

**Protocolos de Transporte**:
- **TCP (Transmission Control Protocol)**: Confiable, garantiza que los datos lleguen completos y en orden. Como una llamada telefónica.
- **UDP (User Datagram Protocol)**: Rápido pero no garantiza entrega. Como enviar postales.

## El Módulo Socket de Python

### Importación y Tipos de Socket

```python
import socket

# Crear un socket TCP
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Crear un socket UDP
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

**Parámetros**:
- `AF_INET`: Familia de direcciones IPv4
- `SOCK_STREAM`: TCP (flujo de datos confiable)
- `SOCK_DGRAM`: UDP (datagramas)

## Ejemplo Práctico 1: Cliente TCP Básico

```python
import socket

def cliente_basico():
    # Crear socket TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor (Google en puerto 80)
        cliente.connect(('www.google.com', 80))
        print("Conectado exitosamente!")
        
        # Enviar una petición HTTP básica
        peticion = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
        cliente.send(peticion.encode('utf-8'))
        
        # Recibir respuesta (primeros 1024 bytes)
        respuesta = cliente.recv(1024)
        print("Respuesta del servidor:")
        print(respuesta.decode('utf-8'))
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cliente.close()

# Ejecutar
cliente_basico()
```

## Ejemplo Práctico 2: Servidor TCP Simple

```python
import socket
import threading

def manejar_cliente(conexion, direccion):
    """Función para manejar cada cliente en un hilo separado"""
    print(f"Cliente conectado desde {direccion}")
    
    try:
        while True:
            # Recibir datos del cliente
            datos = conexion.recv(1024)
            if not datos:
                break
                
            mensaje = datos.decode('utf-8')
            print(f"Mensaje recibido: {mensaje}")
            
            # Enviar respuesta de vuelta
            respuesta = f"Servidor recibió: {mensaje}"
            conexion.send(respuesta.encode('utf-8'))
            
    except Exception as e:
        print(f"Error con cliente {direccion}: {e}")
    
    finally:
        conexion.close()
        print(f"Cliente {direccion} desconectado")

def servidor_tcp():
    # Crear socket servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permitir reutilizar la dirección
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Enlazar a dirección y puerto
    servidor.bind(('localhost', 8888))
    
    # Escuchar conexiones (máximo 5 en cola)
    servidor.listen(5)
    print("Servidor escuchando en localhost:8888")
    
    try:
        while True:
            # Aceptar conexión
            conexion, direccion = servidor.accept()
            
            # Crear hilo para manejar cliente
            hilo_cliente = threading.Thread(
                target=manejar_cliente, 
                args=(conexion, direccion)
            )
            hilo_cliente.daemon = True
            hilo_cliente.start()
            
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
    
    finally:
        servidor.close()

# Ejecutar servidor
servidor_tcp()
```

## Ejemplo Práctico 3: Cliente para Probar el Servidor

```python
import socket
import time

def cliente_para_servidor():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor local
        cliente.connect(('localhost', 8888))
        
        # Enviar varios mensajes
        mensajes = ["Hola servidor!", "¿Cómo estás?", "Enviando datos", "Adiós"]
        
        for mensaje in mensajes:
            cliente.send(mensaje.encode('utf-8'))
            respuesta = cliente.recv(1024)
            print(f"Respuesta: {respuesta.decode('utf-8')}")
            time.sleep(1)
            
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cliente.close()

# Ejecutar cliente
cliente_para_servidor()
```

## Ejemplo Práctico 4: Comunicación UDP

**Servidor UDP:**

```python
import socket

def servidor_udp():
    # Crear socket UDP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('localhost', 9999))
    
    print("Servidor UDP escuchando en localhost:9999")
    
    try:
        while True:
            # Recibir datos (UDP no mantiene conexión)
            datos, direccion_cliente = servidor.recvfrom(1024)
            mensaje = datos.decode('utf-8')
            print(f"Recibido de {direccion_cliente}: {mensaje}")
            
            # Enviar respuesta
            respuesta = f"Eco: {mensaje}"
            servidor.sendto(respuesta.encode('utf-8'), direccion_cliente)
            
    except KeyboardInterrupt:
        print("\nCerrando servidor UDP...")
    
    finally:
        servidor.close()

servidor_udp()
```

**Cliente UDP:**

```python
import socket

def cliente_udp():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor_direccion = ('localhost', 9999)
    
    try:
        mensajes = ["Mensaje UDP 1", "Mensaje UDP 2", "Prueba UDP"]
        
        for mensaje in mensajes:
            # Enviar mensaje (no necesita conexión previa)
            cliente.sendto(mensaje.encode('utf-8'), servidor_direccion)
            
            # Recibir respuesta
            respuesta, servidor_addr = cliente.recvfrom(1024)
            print(f"Respuesta: {respuesta.decode('utf-8')}")
            
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cliente.close()

cliente_udp()
```

## Ejemplo Práctico 5: Chat Simple

**Servidor de Chat:**

```python
import socket
import threading

class ServidorChat:
    def __init__(self):
        self.clientes = []
        self.nicknames = []
        
    def broadcast(self, mensaje):
        """Enviar mensaje a todos los clientes"""
        for cliente in self.clientes:
            try:
                cliente.send(mensaje)
            except:
                # Cliente desconectado, remover
                self.remover_cliente(cliente)
    
    def remover_cliente(self, cliente):
        if cliente in self.clientes:
            index = self.clientes.index(cliente)
            self.clientes.remove(cliente)
            nickname = self.nicknames[index]
            self.nicknames.remove(nickname)
            self.broadcast(f"{nickname} abandonó el chat!".encode('utf-8'))
            cliente.close()
    
    def manejar_cliente(self, cliente):
        while True:
            try:
                mensaje = cliente.recv(1024)
                if mensaje:
                    self.broadcast(mensaje)
                else:
                    self.remover_cliente(cliente)
                    break
            except:
                self.remover_cliente(cliente)
                break
    
    def iniciar_servidor(self):
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('localhost', 7777))
        servidor.listen()
        
        print("Servidor de chat iniciado en localhost:7777")
        
        while True:
            cliente, direccion = servidor.accept()
            print(f"Cliente conectado desde {direccion}")
            
            # Pedir nickname
            cliente.send("NICK".encode('utf-8'))
            nickname = cliente.recv(1024).decode('utf-8')
            
            self.nicknames.append(nickname)
            self.clientes.append(cliente)
            
            print(f"Nickname del cliente: {nickname}")
            self.broadcast(f"{nickname} se unió al chat!".encode('utf-8'))
            
            # Iniciar hilo para manejar cliente
            hilo = threading.Thread(target=self.manejar_cliente, args=(cliente,))
            hilo.start()

# Ejecutar servidor
chat_servidor = ServidorChat()
chat_servidor.iniciar_servidor()
```

**Cliente de Chat:**

```python
import socket
import threading

def recibir_mensajes(cliente):
    """Función para recibir mensajes del servidor"""
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje == "NICK":
                cliente.send(nickname.encode('utf-8'))
            else:
                print(mensaje)
        except:
            print("Error al recibir mensaje")
            cliente.close()
            break

def cliente_chat():
    global nickname
    nickname = input("Elige un nickname: ")
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 7777))
    
    # Iniciar hilo para recibir mensajes
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_recibir.daemon = True
    hilo_recibir.start()
    
    # Enviar mensajes
    while True:
        mensaje = f"{nickname}: {input('')}"
        cliente.send(mensaje.encode('utf-8'))

cliente_chat()
```

## Métodos Importantes del Módulo Socket

### Métodos de Socket TCP (Servidor)
- `bind((host, puerto))`: Enlaza socket a dirección específica
- `listen(backlog)`: Escucha conexiones entrantes
- `accept()`: Acepta conexión, retorna (socket_cliente, dirección)
- `close()`: Cierra el socket

### Métodos de Socket TCP (Cliente)
- `connect((host, puerto))`: Conecta a servidor remoto
- `send(datos)`: Envía datos
- `recv(tamaño)`: Recibe datos (máximo tamaño especificado)

### Métodos de Socket UDP
- `sendto(datos, dirección)`: Envía datos a dirección específica
- `recvfrom(tamaño)`: Recibe datos, retorna (datos, dirección_origen)

### Opciones de Socket
```python
# Permitir reutilizar dirección
socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configurar timeout
socket.settimeout(5.0)  # 5 segundos

# Socket no bloqueante
socket.setblocking(False)
```

## Manejo de Errores Comunes

```python
import socket

def cliente_con_manejo_errores():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('ejemplo.com', 80))
        
    except socket.gaierror as e:
        print(f"Error de resolución DNS: {e}")
        
    except socket.timeout as e:
        print(f"Timeout de conexión: {e}")
        
    except ConnectionRefusedError as e:
        print(f"Conexión rechazada: {e}")
        
    except Exception as e:
        print(f"Error general: {e}")
        
    finally:
        try:
            cliente.close()
        except:
            pass
```

## Consejos Prácticos

1. **Siempre cierra los sockets** usando `close()` o mejor aún, usa `with` statement cuando sea posible
2. **Maneja las excepciones** adecuadamente
3. **Para servidores**, usa threading o asyncio para manejar múltiples clientes
4. **Codifica/decodifica** los datos correctamente (UTF-8 es recomendado)
5. **Usa SO_REUSEADDR** en servidores para evitar errores de "dirección ya en uso"

Los sockets son la base de toda comunicación en red en Python, desde aplicaciones web hasta juegos multijugador, sistemas de chat, y servicios distribuidos. ¡Con estos ejemplos puedes empezar a construir tus propias aplicaciones de red!