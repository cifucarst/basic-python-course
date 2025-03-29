# Ejercicio 5: Generador de Códigos 2FA (TOTP)
# En este reto, vas a programar tu propio generador de códigos 2FA (Two-Factor Authentication) basado en TOTP (Time-Based One-Time Passwords).

# 🛡️ Objetivo: Implementar una función en Python que genere códigos de 6 dígitos basados en una clave secreta y el tiempo actual.

# 📌 Requisitos de la función
# Crea la función generar_codigo_2fa(clave_secreta: str) -> str, que:
# ✅ Use el algoritmo HMAC-SHA1 para generar un código basado en la hora actual.
# ✅ Tome la clave secreta (clave_secreta) como entrada (una cadena en Base32, como en Google Authenticator).
# ✅ Reduzca el código a 6 dígitos (como hacen las apps de autenticación).
# ✅ Cambie cada 30 segundos, como en los sistemas 2FA reales.

# 💡 Pista:
# Usa la librería base64, hmac, hashlib y time.

# 🔹 Ejemplo de uso

# clave = "JBSWY3DPEHPK3PXP"  # Ejemplo de clave secreta en Base32
# print(generar_codigo_2fa(clave))  # Debería imprimir un código de 6 dígitos