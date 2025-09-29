#Gestor de contraseñas simples Crea una clase Password con un atributo valor.

    # Método para verificar si la contraseña tiene al menos 8 caracteres.
    # Método para mostrarla enmascarada (********).

class Password:
    def __init__(self, contrasena):
        self.__contrasena = contrasena

    def verificar_longitud(self):
        if len(self.__contrasena) >= 8:
            return True
        return False

    def mostrar_contrasena_enmascarada(self):
        longitud = len(self.__contrasena)
        return f"contrasena = {'*' * longitud}"


pass1 = Password("12345")
print(pass1.verificar_longitud()) # False
print(pass1.mostrar_contrasena_enmascarada()) # contrasena = *****


#####################################################################


# Mejora

class Password:
    def __init__(self, valor: str):
        self.__valor = valor

    def verificar_longitud(self) -> bool:
        return len(self.__valor) >= 8

    def mostrar_enmascarada(self, mostrar_ultimos: int = 0) -> str:
        """
        Devuelve la contraseña enmascarada.
        - mostrar_ultimos: cantidad de caracteres visibles al final.
        """
        longitud = len(self.__valor)
        if mostrar_ultimos > 0 and mostrar_ultimos < longitud:
            return "*" * (longitud - mostrar_ultimos) + self.__valor[-mostrar_ultimos:]
        return "*" * longitud


# Ejemplo de uso
pass1 = Password("12345")
print(pass1.verificar_longitud())          # False
print(pass1.mostrar_enmascarada())         # *****
print(pass1.mostrar_enmascarada(2))        # ***45

pass2 = Password("supersecreta")
print(pass2.verificar_longitud())          # True
print(pass2.mostrar_enmascarada())         # ************
print(pass2.mostrar_enmascarada(4))        # ********reta
