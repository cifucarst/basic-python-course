# Primera letra en mayúscula
# Escribe un programa que reciba una frase y convierta la primera 
# letra de cada palabra en mayúscula.

def capitalizar_oraciones(frase: str) -> str:
    """Convierte la primera letra de cada oración a mayúscula.

    Args:
        frase (str): La frase a procesar.

    Returns:
        str: La frase con cada oración capitalizada.
    """
    oraciones = frase.split(". ")
    oraciones_capitalizadas = [oracion.capitalize() for oracion in oraciones]
    return ". ".join(oraciones_capitalizadas)

if __name__ == '__main__':
    frase = "python es el mejor lenguaje. es muy popular."
    print(capitalizar_oraciones(frase))
