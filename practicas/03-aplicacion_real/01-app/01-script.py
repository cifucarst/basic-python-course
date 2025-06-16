# 1. Gestión de Usuarios con Hashing Seguro
# Objetivo: Implementar un sistema de registro y autenticación de usuarios usando bcrypt para almacenar contraseñas de forma segura.

# Ejercicio:

# Crea una función para registrar usuarios almacenando su contraseña en formato hash.
# Crea otra función para autenticar usuarios verificando la contraseña ingresada con el hash almacenado.
# Usa bcrypt para el hashing y la verificación de contraseñas.

# Pistas:

    # Usa bcrypt.hashpw() para cifrar contraseñas.
    # Usa bcrypt.checkpw() para validarlas.

import bcrypt

class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = self.hash_password(password)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)
    
    def verify_password(self, password):
        if bcrypt.checkpw(password.encode(), self.password):
            print("Contrasenas correctas")
        else:
            print("Contrasenas incorrectas")
    
    def __str__(self):
        return f"User name: {self.name}, password: {self.password}" # solo mostramos la contrasena para fines practicos, no se usa en la vida real

user1 = Users("Juan", "password")
print(user1)
user1.verify_password("passwod") # no coinciden