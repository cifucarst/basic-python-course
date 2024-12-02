# Buscar y reemplazar
# Escribe un programa que reciba una cadena y dos palabras: una 
# para buscar y otra para reemplazar. El programa debe imprimir la 
# nueva cadena con los cambios.

def reemplazar(cadena: str, palabra_a_buscar: str, palabra_a_reemplazar: str) -> str:
    """Busca y reemplaza una palabra en una frase.

    Args:
        cadena (str): La palabra o frase a evaluar.
        palabra_a_buscar (str): La palabra a buscar en la frase.
        palabra_a_reemplazar (str): La palabra con la que se reemplazará.

    Returns:
        str: Frase con la palabra reemplazada o un mensaje indicando que no se encontró la palabra.
    """
    if palabra_a_buscar in cadena:
        return cadena.replace(palabra_a_buscar, palabra_a_reemplazar)
    else:
        return f'La palabra "{palabra_a_buscar}" no está en la frase.'

def run():
    cadena = input('Escribe la frase original: ')
    palabra_a_buscar = input('¿Qué palabra deseas buscar? ')
    palabra_a_reemplazar = input('¿Con qué palabra deseas reemplazarla? ')

    # Verifica que no haya entradas vacías
    if cadena.strip() and palabra_a_buscar.strip() and palabra_a_reemplazar.strip():
        resultado = reemplazar(cadena, palabra_a_buscar, palabra_a_reemplazar)
        print(f'\nResultado:\n{resultado}')
    else:
        print('Por favor, asegúrate de ingresar una frase y palabras válidas.')

if __name__ == '__main__':
    run()