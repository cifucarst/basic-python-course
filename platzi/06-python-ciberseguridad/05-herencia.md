____

### **Lección: Herencia en POO**

La **herencia** permite que una clase (llamada "clase hija") herede atributos y métodos de otra clase (llamada "clase padre"). Esto es útil para evitar duplicar código cuando varias clases tienen comportamientos similares.

#### **Ejemplo práctico en ciberseguridad: Gestión de usuarios con roles específicos**

Imaginemos un sistema donde hay diferentes tipos de usuarios: administradores, usuarios regulares e invitados. Cada tipo de usuario tiene permisos específicos.

```python
# Clase padre
class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Rol: {self.rol}")

    def acceder_sistema(self):
        print(f"{self.nombre} ha accedido al sistema como {self.rol}.")


# Clases hijas con comportamientos específicos
class Administrador(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "admin")  # Usamos el constructor de la clase padre

    def gestionar_usuarios(self):
        print(f"{self.nombre} está gestionando usuarios.")


class UsuarioRegular(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "usuario")

    def cambiar_contrasena(self):
        print(f"{self.nombre} ha cambiado su contraseña.")


class Invitado(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "invitado")

    def acceso_limitado(self):
        print(f"{self.nombre} solo puede acceder a contenido público.")
```

#### **Ejemplo de uso**

```python
# Creamos diferentes tipos de usuarios
admin = Administrador("Andrés")
usuario = UsuarioRegular("Carlos")
invitado = Invitado("Luis")

# Mostramos información
admin.mostrar_informacion()
usuario.mostrar_informacion()
invitado.mostrar_informacion()

# Acciones específicas
admin.gestionar_usuarios()
usuario.cambiar_contrasena()
invitado.acceso_limitado()

# Método común para todos
admin.acceder_sistema()
usuario.acceder_sistema()
invitado.acceder_sistema()
```

---

### **Tarea práctica 3**

1. Modifica el código anterior para agregar una función de **registro de actividad** que registre en un archivo de texto las acciones realizadas por cada usuario. Por ejemplo:
    
    - Cuando un administrador gestiona usuarios, debe registrar: `"[Fecha y hora] Andrés (admin) gestionó usuarios."`
    - Cuando un usuario regular cambia su contraseña, debe registrar: `"[Fecha y hora] Carlos (usuario) cambió su contraseña."`
    
    **Pista:** Usa el módulo `datetime` para registrar la fecha y hora.
    
2. Añade un método llamado `ver_logs()` exclusivo de los administradores para que puedan leer las actividades registradas en el archivo.
    

---

### **Avance hacia Polimorfismo**

En la próxima lección, veremos cómo diferentes clases pueden compartir un método con el mismo nombre, pero con implementaciones distintas. Esto te ayudará a diseñar sistemas más flexibles.