____


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
        return self.contrasena == hashlib.sha256(contrasena.encode()).hexdigest()

    def cambiar_contrasena(self, contrasena_actual, nueva_contrasena):
        # Verificamos si la contraseña actual es correcta
        if self.verificar_contrasena(contrasena_actual):
            # Actualizamos la contraseña con la nueva, cifrada
            self.contrasena = hashlib.sha256(nueva_contrasena.encode()).hexdigest()
            print("Contraseña cambiada exitosamente.")
        else:
            print("Error: La contraseña actual es incorrecta.")

    def cambiar_rol(self, otro_usuario, nuevo_rol):
        # Cambiar el rol de otro usuario
        if self.rol == "admin":
            otro_usuario.rol = nuevo_rol
            print(f"Rol de {otro_usuario.nombre} cambiado a {nuevo_rol}.")
        else:
            print("No tienes permisos para cambiar roles.")

    def eliminar_usuario(self, usuarios, nombre_usuario):
        # Eliminar un usuario por su nombre
        if self.rol == "admin":
            for usuario in usuarios:
                if usuario.nombre == nombre_usuario:
                    usuarios.remove(usuario)
                    print(f"Usuario {nombre_usuario} eliminado exitosamente.")
                    return
            print("Usuario no encontrado.")
        else:
            print("No tienes permisos para eliminar usuarios.")

    def realizar_accion_admin(self, usuarios):
        # Solo permite realizar acciones si es admin
        if self.rol == "admin":
            while True:
                print("""
                Selecciona una acción administrativa:
                1. Cambiar contraseña
                2. Cambiar rol de un usuario
                3. Eliminar un usuario
                4. Salir
                """)
                opcion = input("Ingresa el número de la opción: ")
                if opcion == "1":
                    contrasena_actual = input("Ingresa tu contraseña actual: ")
                    nueva_contrasena = input("Ingresa la nueva contraseña: ")
                    self.cambiar_contrasena(contrasena_actual, nueva_contrasena)
                elif opcion == "2":
                    nombre_usuario = input("Ingresa el nombre del usuario a modificar: ")
                    nuevo_rol = input("Ingresa el nuevo rol (admin, usuario, invitado): ")
                    for usuario in usuarios:
                        if usuario.nombre == nombre_usuario:
                            self.cambiar_rol(usuario, nuevo_rol)
                            break
                    else:
                        print("Usuario no encontrado.")
                elif opcion == "3":
                    nombre_usuario = input("Ingresa el nombre del usuario a eliminar: ")
                    self.eliminar_usuario(usuarios, nombre_usuario)
                elif opcion == "4":
                    print("Saliendo del menú administrativo...")
                    break
                else:
                    print("Opción no válida. Inténtalo nuevamente.")
        else:
            print("No tienes permisos administrativos.")

# Creamos objetos de la clase Usuario con diferentes roles
admin = Usuario("Andrés", "admin", "qwerty123")
usuario = Usuario("Carlos", "usuario", "1234")
invitado = Usuario("Luis", "invitado", "password")

# Lista de usuarios
usuarios = [admin, usuario, invitado]

# Mostramos información de los usuarios
for u in usuarios:
    u.mostrar_informacion()

# Verificar acciones de administrador
admin.realizar_accion_admin(usuarios)

# Mostramos información de los usuarios después de las acciones
print("\nEstado de los usuarios después de las acciones:")
for u in usuarios:
    u.mostrar_informacion()
```

---

### **Mejoras realizadas:**

1. **Interacción con otros usuarios**:
    
    - Ahora el administrador puede cambiar roles y eliminar usuarios especificando su nombre.
    - Se utiliza una lista (`usuarios`) para gestionar todos los objetos `Usuario`.
2. **Validación de opciones**:
    
    - Se valida la entrada del usuario en el menú administrativo.
    - Se implementa un bucle para permitir múltiples acciones hasta que el admin decida salir.
3. **Acciones administrativas reales**:
    
    - `cambiar_rol`: Cambia el rol de un usuario especificado.
    - `eliminar_usuario`: Elimina un usuario de la lista.
4. **Mejor manejo de errores**:
    
    - Mensajes claros cuando un usuario no es encontrado o una opción no es válida.