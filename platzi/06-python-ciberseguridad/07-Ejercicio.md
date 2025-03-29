____

### **Código 

```python
import datetime
import os

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

    def eliminar_archivo_de_logs(self):
        try:
            if os.path.exists('registro_actividades.txt'):
                os.remove('registro_actividades.txt')  
                print("El archivo de registro de actividades ha sido eliminado.")
            else:
                print("El archivo de registro de actividades no existe.")
        except Exception as e:
            print(f"Ocurrió un error al intentar eliminar el archivo: {e}")


class UsuarioRegular(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "usuario")

    def cambiar_contrasena(self):
        self.registrar_actividad("Cambió su contraseña")
        print(f"{self.nombre} ha cambiado su contraseña.")

    def ver_mis_actividades(self):
        try:
            with open("registro_actividades.txt", "r") as archivo:
                print(f"--- Actividades de {self.nombre} ---")
                for linea in archivo:
                    if self.nombre in linea:
                        print(linea, end="")
        except FileNotFoundError:
            print("No se encontró el archivo de registro de actividades.")


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

# Eliminar archivo de logs por el admin
admin.eliminar_archivo_de_logs()

# Ver actividades de un usuario específico (solo sus actividades)
usuario.ver_mis_actividades()
```

---

### **Cambios realizados:**

1. **Corrección del nombre del archivo en `eliminar_archivo_de_logs()`.**
    
    - Ahora el método elimina correctamente el archivo `registro_actividades.txt` si existe.
2. **Implementación de `ver_mis_actividades()` en `UsuarioRegular`:**
    
    - Este método lee el archivo de registro y filtra las actividades relacionadas con el nombre del usuario.
    - Solo muestra las líneas que contienen el nombre del usuario actual.
3. **Mensajes mejorados:**
    
    - Mensajes más claros cuando no se encuentra el archivo de registros.
4. **Robustez ante errores:**
    
    - Manejo de excepciones para evitar que el programa se detenga por errores no controlados.

---

### **Resultado esperado:**

1. El administrador puede eliminar el archivo de registro usando `eliminar_archivo_de_logs()`.
2. Los usuarios regulares pueden usar `ver_mis_actividades()` para ver solo las actividades registradas bajo su nombre.
3. Si el archivo no existe, se mostrarán mensajes claros indicando la ausencia del archivo.