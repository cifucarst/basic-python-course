# Reverso de cadena
# Escribe un programa que tome una cadena ingresada por el usuario e imprima la cadena invertida.

def invertir_cadena(cadena: str) -> str:
    """Regresa una cadena invertida.

    Args:
        cadena (str): La cadena de texto a invertir.

    Returns:
        str: La cadena invertida.
    """
    return cadena[::-1]


if __name__ == '__main__':
    cadena = input('Ingresa una cadena de texto: ')
    if cadena.strip():  # Verifica que no esté vacía
        cadena_invertida = invertir_cadena(cadena)
        print(f'Cadena original: {cadena}. Cadena invertida: {cadena_invertida}')
    else:
        print("Por favor, ingresa una cadena válida.")