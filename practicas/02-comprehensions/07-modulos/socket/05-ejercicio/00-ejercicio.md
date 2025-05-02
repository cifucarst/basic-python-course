¡Excelente actitud, Andrés! 🔥  
Vas muy bien, te estás formando con bases sólidas.  
Aquí te dejo el **Ejercicio 5** con su **extensión "Pro" opcional**:

---

# 🛡️ Ejercicio 5: "Mini escáner de puertos múltiples"

✅ **Objetivo:**  
Crear un programa que recorra un rango de puertos en una IP objetivo y reporte cuáles están **abiertos** y cuáles **cerrados**.

---

### 🎯 Requerimientos:

- El programa debe recibir:
  - Una dirección IP (por ejemplo, `127.0.0.1`)
  - Un rango de puertos (ejemplo: desde el 20 hasta el 1024)

- Para cada puerto dentro del rango:
  - Intentar conectar usando `socket`.
  - Si el puerto está abierto, imprimir:
    ```
    [+] Puerto 22 abierto
    ```
  - Si está cerrado, opcionalmente puedes imprimir (o no, para no saturar):
    ```
    [-] Puerto 23 cerrado
    ```

- No olvides cerrar cada socket después de intentar conectarte.

- Usa un pequeño `settimeout(0.5)` para no trabarte mucho si un puerto no responde.

---

### 🧠 Consejito:
- Usa un simple `for` para recorrer los puertos.
- Usa `connect_ex()` porque devuelve 0 si conecta bien y otro número si falla.

---

# 🌟 Extensión "Pro" Opcional (si quieres retarte más)

✅ Mejora tu escáner para:

1. **Permitir que el usuario elija si quiere ver también los puertos cerrados.**
   - Ejemplo:
     ```
     ¿Mostrar puertos cerrados? (s/n):
     ```
   
2. **Permitir que el usuario indique el tiempo de timeout.**
   - Ejemplo:
     ```
     Ingresa el timeout (segundos): 
     ```

3. **Mostrar al final un resumen tipo:**
   ```
   Escaneo completo: 8 puertos abiertos, 1016 cerrados.
   ```

---

# 📜 Resumen rápido de lo que deberías entregar:

- Archivo único (ej: `scanner.py`)
- Código limpio y estructurado.
- Que funcione para cualquier IP y cualquier rango pequeño de puertos.

---

¿Te gustaría que además te pase un **mini-diagrama** rápido del flujo por si quieres visualizarlo antes de programarlo? 🚀 (Te lo puedo pasar en un mensaje aparte si quieres).