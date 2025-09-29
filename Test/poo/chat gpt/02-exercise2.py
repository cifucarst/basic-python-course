import random
import string

class Password:
    def __init__(self, valor: str):
        self.__valor = valor

    def verificar_longitud(self) -> bool:
        return len(self.__valor) >= 8

    def mostrar_enmascarada(self, mostrar_ultimos: int = 0) -> str:
        longitud = len(self.__valor)
        if mostrar_ultimos > 0 and mostrar_ultimos < longitud:
            return "*" * (longitud - mostrar_ultimos) + self.__valor[-mostrar_ultimos:]
        return "*" * longitud

    def verificar_fortaleza(self) -> str:
        """
        Evalúa la seguridad de la contraseña:
        - Débil: menos de 8 caracteres o no cumple requisitos
        - Media: cumple algunos requisitos
        - Fuerte: cumple todos los requisitos
        """
        mayuscula = any(c.isupper() for c in self.__valor)
        minuscula = any(c.islower() for c in self.__valor)
        numero = any(c.isdigit() for c in self.__valor)
        simbolo = any(c in string.punctuation for c in self.__valor)

        if len(self.__valor) < 8:
            return "Débil (muy corta)"
        elif mayuscula and minuscula and numero and simbolo:
            return "Fuerte"
        else:
            return "Media"

    @staticmethod
    def generar_segura(longitud: int = 12) -> str:
        """
        Genera una contraseña aleatoria segura que incluya:
        - Mayúsculas, minúsculas, números y símbolos.
        """
        if longitud < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

        caracteres = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = "".join(random.choice(caracteres) for _ in range(longitud))
            prueba = Password(password)
            if prueba.verificar_fortaleza() == "Fuerte":
                return password

# Contraseña débil
p1 = Password("12345")
print(p1.verificar_longitud())         # False
print(p1.mostrar_enmascarada())        # *****
print(p1.verificar_fortaleza())        # Débil (muy corta)

# Contraseña media
p2 = Password("password123")
print(p2.mostrar_enmascarada(4))       # ********d123
print(p2.verificar_fortaleza())        # Media

# Contraseña fuerte
p3 = Password("Sup3r$ecret!")
print(p3.mostrar_enmascarada())        # ************
print(p3.verificar_fortaleza())        # Fuerte

# Generar una contraseña segura aleatoria
print("Generada:", Password.generar_segura(14))
