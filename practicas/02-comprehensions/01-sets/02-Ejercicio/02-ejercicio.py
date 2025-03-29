from typing import Set

usuarios_conectados = {"alice", "bob", "charlie", "dave"}
usuarios_bloqueados = {"charlie", "eve", "dave"}

def usuarios_a_desconectar(conectados: Set[str], bloqueados: Set[str]) -> Set[str]:
    """Devuelve un conjunto con los usuarios conectados que están en la lista de bloqueados."""
    return conectados & bloqueados  # Alternativa a intersection()

result = usuarios_a_desconectar(usuarios_conectados, usuarios_bloqueados)
print(f"Usuarios a desconectar: {result}")