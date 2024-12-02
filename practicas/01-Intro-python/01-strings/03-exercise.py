# Palíndromo
# Crea un programa que determine si una cadena ingresada por el 
# usuario es un palíndromo (se lee igual de izquierda a derecha 
# que de derecha a izquierda). Ignora mayúsculas, minúsculas y 
# espacios.

import re

def es_palindromo(palabra: str) -> bool:
    """Determina si una palabra o frase es un palíndromo.

    Args:
        palabra (str): La palabra o frase a evaluar.

    Returns:
        bool: True si es un palíndromo, False en caso contrario.
    """
    palabra = re.sub(r'[^a-zA-Z0-9]', '', palabra).lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida

def run():
    palabra = input('Escribe una palabra o frase: ')
    if palabra.strip():  # Verifica que no esté vacía
        if es_palindromo(palabra):
            print('Es un palíndromo.')
        else:
            print('No es un palíndromo.')
    else:
        print('Por favor, ingresa una palabra o frase válida.')

if __name__ == '__main__':
    run()