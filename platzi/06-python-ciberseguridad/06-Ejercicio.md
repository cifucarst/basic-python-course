
___

### **Código 

```python
import datetime

# Clase padre
class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Rol: {self.rol}")

    def acceder_sistema(self):
        self.registrar_actividad(f"Accedió al sistema como {self.rol}")
        print(f"{self.nombre} ha accedido al sistema como {self.rol}.")

    def registrar_actividad(self, actividad):
        ahora = datetime.datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
        with open("registro_actividades.txt", "a") as archivo:
            archivo.write(f"[{fecha_hora}] {self.nombre} ({self.rol}) {actividad}.\n")


# Clases hijas con comportamientos específicos
class Administrador(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "admin")  # Usamos el constructor de la clase padre

    def gestionar_usuarios(self):
        self.registrar_actividad("Gestionó usuarios")
        print(f"{self.nombre} está gestionando usuarios.")

    def ver_logs(self):
        try:
            with open("registro_actividades.txt", "r") as archivo:
                print("--- Registro de actividades ---")
                for linea in archivo:
                    print(linea, end="")
        except FileNotFoundError:
            print("No se encontró el archivo de registro de actividades.")


class UsuarioRegular(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "usuario")

    def cambiar_contrasena(self):
        self.registrar_actividad("Cambió su contraseña")
        print(f"{self.nombre} ha cambiado su contraseña.")


class Invitado(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "invitado")

    def acceso_limitado(self):
        self.registrar_actividad("Accedió a contenido público")
        print(f"{self.nombre} solo puede acceder a contenido público.")


# Creamos diferentes tipos de usuarios
admin = Administrador("Andrés")
usuario = UsuarioRegular("Carlos")
invitado = Invitado("Luis")

# Mostramos información
admin.mostrar_informacion()
usuario.mostrar_informacion()
invitado.mostrar_informacion()
print("\n")

# Acciones específicas
admin.gestionar_usuarios()
usuario.cambiar_contrasena()
invitado.acceso_limitado()
print("\n")

# Método común para todos
admin.acceder_sistema()
usuario.acceder_sistema()
invitado.acceder_sistema()
print("\n")

# Ver logs (solo para administradores)
admin.ver_logs()

# Comentado: Esto causaría un error porque solo el admin tiene ver_logs()
# usuario.ver_logs()
```

---

### **Cambios realizados:**

1. **Control de errores en `ver_logs()`:** Si el archivo de registro no existe, ahora se muestra un mensaje indicando que no se encontró, en lugar de lanzar una excepción.
    
    ```python
    except FileNotFoundError:
        print("No se encontró el archivo de registro de actividades.")
    ```
    
2. **Eliminado `usuario.ver_logs()`:** El método `ver_logs()` es exclusivo de los administradores. Intentar llamarlo desde `usuario` o `invitado` no tiene sentido, ya que no está definido para esas clases.
    
3. **Comentarios adicionales:** Agregué explicaciones en el código para facilitar el aprendizaje y resaltar los puntos clave.
    

---

### **Prueba de ejecución**

Al ejecutar este código:

1. Se crearán tres usuarios: un administrador, un usuario regular y un invitado.
2. Cada uno realizará acciones específicas.
3. Todas las actividades serán registradas en el archivo `registro_actividades.txt`.
4. Solo el administrador podrá leer los registros con `ver_logs()`.

### **Tarea extra (opcional):**

1. Implementa un método en la clase `Administrador` para **eliminar el archivo de registro de actividades**, asegurando que solo los administradores puedan hacerlo.
    - **Pista:** Usa el módulo `os` para eliminar archivos.
2. Permite que los usuarios regulares puedan ver solo sus propias actividades en el archivo de registro.