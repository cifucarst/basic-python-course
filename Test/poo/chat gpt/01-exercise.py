# Usuario de sistema Crea una clase Usuario con atributos: nombre, correo, rol.

# Método para mostrar la información del usuario.
# Método para verificar si el rol es "admin"

class Usuario:
    def __init__(self, nombre: str, correo: str, rol: str):
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def __str__(self):
        return f"Nombre del usuario: {self.nombre}, con correo: {self.correo}, Es usuario administrador? {'si' if self.rol == 'admin' else 'no'}"

    def verificar_rol(self):
        if self.rol == 'admin':
            return True
        return False
    
usuario1 = Usuario("Elkin", "Ekin_avion@gmail.com", "admin")
print(usuario1)

usuario2 = Usuario("Oscar", "Oscar_cantina@gmail.com", "empleado")
print(usuario2)


####################################################################################

# correccion

class Usuario:
    def __init__(self, nombre: str, correo: str, rol: str):
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}"

    def verificar_rol(self) -> bool:
        return self.rol.lower() == "admin"


# Ejemplo de uso
usuario1 = Usuario("Elkin", "ekin_avion@gmail.com", "admin")
usuario2 = Usuario("Oscar", "oscar_cantina@gmail.com", "empleado")

print(usuario1)
print("¿Es administrador?", "Sí" if usuario1.verificar_rol() else "No")

print(usuario2)
print("¿Es administrador?", "Sí" if usuario2.verificar_rol() else "No")
