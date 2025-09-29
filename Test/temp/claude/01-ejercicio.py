def evaluar_password(password):
    if len(password) >= 8:  # >= no >, porque 8 caracteres ya cumple
        tiene_mayuscula = any(c.isupper() for c in password)
        tiene_minuscula = any(c.islower() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        
        return tiene_mayuscula and tiene_minuscula and tiene_numero
    return False


# Prueba tu función
passwords = ["123456", "Password123", "pass", "MiPassword123"]
for pwd in passwords:
    print(f"{pwd}: {evaluar_password(pwd)}")