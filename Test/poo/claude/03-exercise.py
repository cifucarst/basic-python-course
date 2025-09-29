# Ejercicio 1: Clase Usuario Básica
# Crea una clase Usuario con los siguientes atributos:

# nombre (string)
# email (string)
# contraseña (string, privada)
# activo (boolean, por defecto True)
# Implementa métodos para:

# cambiar_contraseña(nueva_contraseña): cambia la contraseña
# desactivar_usuario(): cambia el estado a inactivo
# mostrar_info(): muestra nombre, email y estado (sin mostrar contraseña)

class Usuario:
    def __init__(self, nombre: str, email: str, contraseña: str):
        self.nombre = nombre
        self.email = email
        self.__contraseña = contraseña  # Atributo privado
        self.activo: bool = True  # Por defecto es True

    def cambiar_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    def desactivar_usuario(self):
        self.activo = False

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f"Nombre: {self.nombre}, Email: {self.email}, Estado: {estado}")

# Ejemplo de uso
usuario1 = Usuario("Juan Perez", "juan.perez@gmail.com", "mi_contraseña123")
usuario1.mostrar_info()  # Muestra la información del usuario
usuario1.cambiar_contraseña("nueva_contraseña456")  # Cambia la contraseña
usuario1.desactivar_usuario()  # Desactiva el usuario
usuario1.mostrar_info()  # Muestra la información del usuario nuevamente




################################################################################

# Mejora del ejercicio

import re

class Usuario:
    def __init__(self, nombre: str, email: str, contraseña: str):
        # Validaciones
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string no vacío")
        if not self._validar_email(email):
            raise ValueError("Email inválido")
        if len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        
        self.nombre = nombre.strip()
        self.email = email.lower().strip()
        self.__contraseña = contraseña
        self.activo: bool = True

    def _validar_email(self, email: str) -> bool:
        """Valida formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))

    def cambiar_contraseña(self, nueva_contraseña: str):
        """Cambia la contraseña del usuario"""
        if not nueva_contraseña or len(nueva_contraseña) < 8:
            raise ValueError("La nueva contraseña debe tener al menos 8 caracteres")
        self.__contraseña = nueva_contraseña
        print("Contraseña cambiada exitosamente")

    def desactivar_usuario(self):
        """Desactiva el usuario"""
        self.activo = False
        print(f"Usuario {self.nombre} desactivado")

    def activar_usuario(self):
        """Reactiva el usuario"""
        self.activo = True
        print(f"Usuario {self.nombre} activado")

    def verificar_contraseña(self, contraseña: str) -> bool:
        """Verifica si la contraseña proporcionada es correcta"""
        return self.__contraseña == contraseña

    def mostrar_info(self):
        """Muestra información del usuario (sin contraseña)"""
        estado = "Activo" if self.activo else "Inactivo"
        print(f"Nombre: {self.nombre}, Email: {self.email}, Estado: {estado}")