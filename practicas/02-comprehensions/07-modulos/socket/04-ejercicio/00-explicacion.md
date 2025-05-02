Antes de que programes el **Ejercicio 4 (Cliente-Servidor de eco)**, te paso un **mini diagrama de flujo** sencillo para que visualices bien cómo funciona:

---

## 🎯 Diagrama de flujo - Cliente-Servidor de Eco

```
Servidor:                      Cliente:
--------------------------------------------
[Iniciar servidor TCP]          [Iniciar cliente TCP]
        ↓                               ↓
[Escuchar conexiones]            [Conectarse al servidor]
        ↓                               ↓
[Aceptar cliente]                [Enviar mensaje al servidor]
        ↓                               ↓
[Recibir mensaje del cliente]    [Esperar respuesta]
        ↓                               ↓
[Enviar de vuelta el mismo       [Recibir mensaje eco]
 mensaje recibido (eco)]                ↓
        ↓                        [Mostrar respuesta]
[Sigue esperando más mensajes]   [Cerrar conexión si se desea]
```

---

## 🛠️ ¿Qué debe hacer cada uno?

- **Servidor:**
  - Espera a que un cliente se conecte.
  - Cuando recibe un mensaje, simplemente **lo devuelve**.
  - Sigue funcionando hasta que el cliente se desconecte.

- **Cliente:**
  - Se conecta al servidor.
  - Envía un mensaje.
  - Recibe el "eco" (el mismo mensaje que envió).
  - Puede enviar más mensajes o cerrar la conexión.

---

### 📦 Detalles técnicos que debes incluir:
- Usa `recv()` para recibir datos.
- Usa `sendall()` para enviar la respuesta.
- Controla si el cliente se desconecta (mensaje vacío).

---

¿Listo para que te formule oficialmente el **Ejercicio 4**? 🚀  
¿Quieres además que te dé una pequeña *pista extra* para que lo hagas más fluido? 🎯 (opcional).