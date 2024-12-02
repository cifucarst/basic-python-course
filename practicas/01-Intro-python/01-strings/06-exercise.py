# Frecuencia de caracteres
# Escribe un programa que reciba una cadena y cuente la frecuencia de cada 
# carácter en la cadena, imprimiendo el resultado en un formato 
# amigable.

from collections import Counter

def contar_frecuencia_caracteres(cadena):
    """Cuenta la frecuencia de cada carácter en una cadena.

    Args:
        cadena (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias.
    """

    # Convertimos la cadena a minúsculas para una comparación más sencilla
    cadena = cadena.lower()
    # Utilizamos Counter para contar las ocurrencias de cada carácter
    contador = Counter(cadena)
    return contador

if __name__ == "__main__":
    cadena = input("Ingrese una cadena: ")
    frecuencias = contar_frecuencia_caracteres(cadena)

    print("Frecuencia de cada carácter:")
    for caracter, frecuencia in frecuencias.items():
        print(f"{caracter}: {frecuencia}")