# 7. UserDict, UserList, UserString
# Estas clases permiten crear estructuras de datos personalizadas basadas en diccionarios, listas o cadenas. Se usan principalmente para extender funcionalidades.

# Ejemplo: Extender un diccionario

from collections import UserDict

class MiDiccionario(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError("Las claves deben ser cadenas.")
        super().__setitem__(key, value)

mi_diccionario = MiDiccionario()
mi_diccionario["clave"] = "valor"
print(mi_diccionario)  # Salida: {'clave': 'valor'}

# mi_diccionario[123] = "valor"  # Lanza un KeyError