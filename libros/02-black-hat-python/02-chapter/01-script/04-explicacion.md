Excelente trabajo extendiendo el script para mostrar más información. Aquí algunas observaciones interesantes sobre lo que ocurre y cómo podrías seguir mejorándolo:

---

### 🔍 ¿Por qué `google.com` no redirige?
A diferencia de otros sitios que sí usan redirecciones explícitas (`HTTP 301` o `302`), en este caso Google responde directamente con un `HTTP/1.1 200 OK`. Es decir, **no hay redirección** como tal, por eso no aparece ningún encabezado `Location:` que tu script pueda seguir.

---

### 📌 Lo que estás viendo:

```http
HTTP/1.1 200 OK
...
Transfer-Encoding: chunked
...
608d
<!doctype html><html itemscope=...
```

La línea `608d` es parte del **transfer encoding chunked**. Significa que el cuerpo del mensaje HTTP se está enviando en "trozos" (chunks), donde `608d` es el tamaño en hexadecimal del chunk que viene.

---

### 🛠️ Siguientes mejoras posibles:

#### 1. **Leer la respuesta completa (no solo los primeros 9096 bytes)**
Ahora estás leyendo solo una parte con `recv(9096)`. Podrías implementar una función que lea *todo* el contenido usando un bucle hasta que no se reciban más datos:

```python
def recv_all(sock):
    data = b""
    while True:
        part = sock.recv(4096)
        if not part:
            break
        data += part
    return data
```

Y luego reemplazas esta línea:

```python
response = client.recv(9096).decode()
```

por:

```python
response = recv_all(client).decode(errors="replace")
```

#### 2. **Parsear y decodificar correctamente `Transfer-Encoding: chunked`**

Ahora mismo estás mostrando los datos “crudos”. Podrías interpretar los chunks y extraer el HTML limpio. ¿Te gustaría que te ayudara a implementar eso?

#### 3. **Soporte para HTTPS**
Como `google.com` responde con redirección a HTTPS si usas `http://`, no verás eso si llamas directamente a `www.google.com` (porque Google ahora acepta HTTP, pero responde con 200 y contenido HTML). Si probaras por ejemplo con `httpbin.org/redirect-to`, podrías ver el redireccionamiento en acción.

---

### ✅ ¿Qué hacer para probar la redirección?
Prueba con este sitio:

```python
http_request("httpbin.org", 80, "/redirect-to?url=http://example.com")
```

Ese sí responde con:

```
HTTP/1.1 302 FOUND
Location: http://example.com
```

---

¿Te gustaría que mejoremos el script con soporte completo para redirecciones, HTTPS y descifrado de `chunked`? Puedo ayudarte paso a paso con cada una.