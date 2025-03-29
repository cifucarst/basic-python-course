___


```python
# Importamos la biblioteca hashlib para el hash de contraseñas
import hashlib

class Usuario:
    def __init__(self, nombre, rol, contrasena):
        self.nombre = nombre  # Atributo para el nombre del usuario
        self.rol = rol        # Atributo para el rol (ejemplo: admin, usuario, invitado)
        # Ciframos la contraseña utilizando SHA-256
        self.contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

    def mostrar_informacion(self):
        # Método para mostrar información del usuario
        print(f"Nombre: {self.nombre}, Rol: {self.rol}")

    def verificar_contrasena(self, contrasena):
        # Comparamos la contraseña cifrada
        if self.contrasena == hashlib.sha256(contrasena.encode()).hexdigest():
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")

# Creamos un objeto de la clase Usuario
usuario1 = Usuario("Andrés", "admin", "qwerty123")

# Llamamos al método mostrar_informacion
usuario1.mostrar_informacion()

# Verificamos contraseñas
usuario1.verificar_contrasena("qwerty123")  # Correcta
usuario1.verificar_contrasena("qwerty13")   # Incorrecta
```

---

### **Mejoras implementadas:**

1. **Cifrado de contraseñas**:
    
    - Se utiliza `hashlib.sha256` para cifrar la contraseña antes de almacenarla.
    - Esto simula cómo las contraseñas se manejan en sistemas reales, donde nunca se almacenan en texto plano.
2. **Eliminación de contraseñas en `mostrar_informacion`**:
    
    - Por seguridad, no mostramos la contraseña al llamar a este método.
3. **Mensajes más claros en `verificar_contrasena`**:
    
    - Se dan respuestas específicas dependiendo de si la contraseña es correcta o no.

---

### **Tarea adicional:**

1. Modifica la clase para incluir un método llamado `cambiar_contrasena`, que permita al usuario cambiar su contraseña después de verificar la contraseña actual.
2. Crea varios objetos de la clase `Usuario` con diferentes roles (`admin`, `usuario`, `invitado`) y agrega lógica para verificar si un usuario tiene permisos de administrador antes de realizar ciertas acciones (por ejemplo, cambiar la contraseña de otro usuario).