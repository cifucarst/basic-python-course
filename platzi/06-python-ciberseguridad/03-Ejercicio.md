___


### **Código 

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
            return True
        else:
            return False

    def cambiar_contrasena(self, contrasena_actual, nueva_contrasena):
        # Verificamos si la contraseña actual es correcta
        if self.verificar_contrasena(contrasena_actual):
            # Actualizamos la contraseña con la nueva, cifrada
            self.contrasena = hashlib.sha256(nueva_contrasena.encode()).hexdigest()
            print("Contraseña cambiada exitosamente.")
        else:
            print("Error: La contraseña actual es incorrecta.")

# Creamos objetos de la clase Usuario con diferentes roles
admin = Usuario("Andrés", "admin", "qwerty123")
usuario = Usuario("Carlos", "usuario", "1234")
invitado = Usuario("Luis", "invitado", "password")

# Mostramos información de los usuarios
admin.mostrar_informacion()
usuario.mostrar_informacion()
invitado.mostrar_informacion()

# Verificamos contraseñas del usuario admin
if admin.verificar_contrasena("qwerty123"):
    print("Contraseña correcta para el admin.")
else:
    print("Contraseña incorrecta para el admin.")

# Intentamos cambiar la contraseña del admin
admin.cambiar_contrasena("qwerty123", "nueva_contrasena_admin")
admin.cambiar_contrasena("1234", "otra_contrasena")  # Fallará porque la contraseña actual no es correcta
```

---

### **Cambios realizados:**

1. **Método `cambiar_contrasena`**:
    
    - Ahora verifica la contraseña actual antes de permitir el cambio.
    - Imprime mensajes claros para informar si el cambio fue exitoso o no.
2. **Manejo de contraseñas**:
    
    - El atributo `self.contrasena` siempre almacena el valor cifrado, nunca texto plano.
3. **Corrección en la creación de objetos**:
    
    - No sobrescribimos objetos como `usuario1`, evitando confusiones.
4. **Mensajes más claros**:
    
    - Se mejoraron los mensajes para las verificaciones y los cambios de contraseña.

---

### **Tarea adicional:**

1. **Roles y permisos**:
    - Modifica la clase para agregar un método llamado `realizar_accion_admin`, que permita realizar una acción específica (como cambiar la contraseña de otro usuario) solo si el usuario tiene el rol `admin`.
2. **Prueba con diferentes usuarios**:
    - Intenta cambiar la contraseña de otro usuario utilizando un objeto con rol `admin` y otro con rol `usuario`.