# Ejercicio 2: Detección de Correos de Phishing
# Crea una función en Python llamada detectar_phishing(email: str) -> bool que analice un correo electrónico y determine si puede ser sospechoso de phishing.

# Un correo será considerado sospechoso si:
# ✅ Contiene palabras clave como "urgente", "verifica tu cuenta", "ganaste", "gratis", "contraseña", "haz clic aquí".
# ✅ Contiene más de 3 enlaces (http:// o https://).
# ✅ Contiene más de 2 direcciones de correo electrónico (@ en el texto).

# La función debe devolver True si el correo parece sospechoso de phishing y False si no.

# Ejemplo de uso:

# correo1 = "Hola, verifica tu cuenta ahora en http://falso-banco.com para evitar suspensión. Gracias."  
# correo2 = "Hola Juan, recuerda nuestra reunión de mañana. Saludos."  

# print(detectar_phishing(correo1))  # Debe devolver True (phishing)  
# print(detectar_phishing(correo2))  # Debe devolver False (seguro)

import re  

def detectar_phishing(email: str) -> bool:
    palabras_sospechosas = ("urgente", "verifica tu cuenta", "ganaste", "gratis", "contraseña", "haz clic aquí", "falso-banco")
    
    # Verifica si alguna palabra sospechosa está en el correo
    contiene_palabras_sospechosas = any(palabra in email.lower() for palabra in palabras_sospechosas)
    
    # Cuenta cuántos enlaces hay en el correo
    enlaces = re.findall(r"https?://\S+", email)
    cantidad_enlaces = len(enlaces)

    # Cuenta cuántos correos electrónicos hay en el texto
    cantidad_correos = email.count("@")

    # Si cumple alguna condición de phishing, retorna True
    if contiene_palabras_sospechosas or cantidad_enlaces > 3 or cantidad_correos > 2:
        return True  # Sospechoso de phishing
    return False  # Seguro

# Pruebas
correo1 = "Hola, verifica tu cuenta ahora en http://falso-banco.com para evitar suspensión. Gracias."  
correo2 = "Hola Juan, recuerda nuestra reunión de mañana. Saludos."  
correo3 = "¡Ganaste un premio! Haz clic aquí: https://estafa.com y confirma tu contraseña."  
correo4 = "Aquí tienes los documentos. Mi correo es juan@empresa.com, puedes responder a soporte@empresa.com"  

print(detectar_phishing(correo1))  # True  
print(detectar_phishing(correo2))  # False  
print(detectar_phishing(correo3))  # True  
print(detectar_phishing(correo4))  # False  