# Ejercicio 2: Detectar usuarios en listas negras
# Imagina que tienes una lista de usuarios conectados a un sistema y otra lista de usuarios bloqueados. Escribe un programa que determine qué usuarios deben ser desconectados porque están en la lista negra.

# 📌 Instrucciones:

# Crea un conjunto con los usuarios conectados.
# Crea otro conjunto con los usuarios bloqueados.
# Muestra los usuarios conectados que también están en la lista negra.
# 🔹 Ejemplo de entrada:

# usuarios_conectados = {"alice", "bob", "charlie", "dave"}
# usuarios_bloqueados = {"charlie", "eve", "dave"}
# 🔹 Salida esperada:

# Usuarios a desconectar: {'charlie', 'dave'}

from typing import Set

usuarios_conectados = {"alice", "bob", "charlie", "dave"}
usuarios_bloqueados = {"charlie", "eve", "dave"}

def detectar_usuarios_bloqueados(set1: Set[str], set2: Set[str]) -> set[str]:
    return set1.intersection(set2)

result = detectar_usuarios_bloqueados(usuarios_conectados, usuarios_bloqueados)
print(result)