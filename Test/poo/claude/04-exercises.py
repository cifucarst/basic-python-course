# Ejercicio 2: Validador de Contraseñas
# Crea una clase `ValidadorContraseña` que tenga un método estático `es_segura(contraseña)` que verifique:
# - Mínimo 8 caracteres
# - Al menos una letra mayúscula
# - Al menos una letra minúscula  
# - Al menos un número
# - Al menos un carácter especial (!@#$%^&*)

# El método debe retornar `True` si cumple todos los criterios, `False` en caso contrario.

import re

class ValidadorContrasena:
    @staticmethod
    def es_segura(contrasena: str) -> bool:
        """
        Verifica si una contraseña cumple con los criterios de seguridad.

        Args:
            contrasena (str): La contraseña a validar.

        Returns:
            bool: True si la contraseña es segura, False en caso contrario.
        """
        # Criterios de seguridad
        longitud_minima = len(contrasena) >= 8
        tiene_mayuscula = re.search(r'[A-Z]', contrasena) is not None
        tiene_minuscula = re.search(r'[a-z]', contrasena) is not None
        tiene_numero = re.search(r'[0-9]', contrasena) is not None
        tiene_caracter_especial = re.search(r'[!@#$%^&*]', contrasena) is not None

        # Retorna True solo si todos los criterios se cumplen
        return (longitud_minima and 
                tiene_mayuscula and 
                tiene_minuscula and 
                tiene_numero and 
                tiene_caracter_especial)

# Ejemplo de uso
print(f"La contraseña 'Contrasena123!' es segura: {ValidadorContrasena.es_segura('Contrasena123!')}")
print(f"La contraseña 'corto' es segura: {ValidadorContrasena.es_segura('corto')}")
print(f"La contraseña 'SinMayuscula1!' es segura: {ValidadorContrasena.es_segura('sinmayuscula1!')}")