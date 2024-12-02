# Contraseña segura
# Crea un programa que reciba una cadena e indique si cumple con las siguientes reglas para ser una contraseña segura:

#     Al menos 8 caracteres.
#     Contiene al menos una letra mayúscula.
#     Contiene al menos una letra minúscula.
#     Contiene al menos un número.

def es_contrasena_segura(contrasena: str) -> bool:
    """Verifica si una contraseña cumple con los requisitos de seguridad.

    Args:
        contrasena (str): La contraseña a evaluar.

    Returns:
        bool: True si la contraseña es segura, False en caso contrario.
    """
    if len(contrasena) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

        # Si ya se cumplen todos los criterios, salimos del bucle
        if tiene_mayuscula and tiene_minuscula and tiene_numero:
            break

    return tiene_mayuscula and tiene_minuscula and tiene_numero

if __name__ == "__main__":
    contrasena = input("Ingrese su contraseña: ").strip()
    if es_contrasena_segura(contrasena):
        print("✅ La contraseña es segura.")
    else:
        print("❌ La contraseña no es segura.")
        print("Debe cumplir con los siguientes requisitos:")
        print("- Tener al menos 8 caracteres.")
        print("- Incluir al menos una letra mayúscula.")
        print("- Incluir al menos una letra minúscula.")
        print("- Incluir al menos un número.")