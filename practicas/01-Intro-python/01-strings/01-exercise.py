# Conteo de caracteres
# Escribe un programa que reciba una cadena ingresada por el usuario y:

#     Cuente cuántos caracteres tiene.
#     Cuente cuántas vocales contiene.
#     Imprima el resultado.

def contar_caracteres_y_vocales(cadena):
    """Cuenta el número de caracteres alfabéticos y vocales en una cadena.

    Args:
        cadena (str): La cadena de texto a analizar.

    Returns:
        tuple: Una tupla con el número de caracteres alfabéticos y vocales, respectivamente.
    """
    cadena = cadena.lower()
    vocales = "aeiouáéíóú"
    letras = [letra for letra in cadena if letra.isalpha()]
    num_vocales = sum(1 for letra in letras if letra in vocales)
    return len(letras), num_vocales

if __name__ == '__main__':
    cadena = input('Ingresa una cadena de texto: ')
    if cadena.strip():  # Verifica que no esté vacía
        num_caracteres, num_vocales = contar_caracteres_y_vocales(cadena)
        print(f'La cadena ingresada tiene: {num_caracteres} caracteres alfabéticos, además tiene {num_vocales} vocales.')
    else:
        print("Por favor, ingresa una cadena válida.")