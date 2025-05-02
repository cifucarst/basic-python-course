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

import base64
import struct
import time
import hmac
import hashlib

def generar_codigo_2fa(clave_secreta: str) -> str:
    # Paso 1: Decodificar la clave secreta Base32 a bytes
    clave_bytes = base64.b32decode(clave_secreta.upper())

    # Paso 2: Obtener el número de intervalo de tiempo actual (cada 30 segundos)
    intervalo = int(time.time()) // 30

    # Paso 3: Empaquetar el intervalo como un número de 8 bytes (big-endian)
    mensaje = struct.pack(">Q", intervalo)

    # Paso 4: Generar HMAC-SHA1 usando la clave y el tiempo
    hmac_hash = hmac.new(clave_bytes, mensaje, hashlib.sha1).digest()

    # Paso 5: Dynamic truncation para obtener un valor de 4 bytes del HMAC
    offset = hmac_hash[-1] & 0x0F
    codigo_binario = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF

    # Paso 6: Obtener los últimos 6 dígitos
    codigo_otp = codigo_binario % 1000000

    # Retornar como string con ceros a la izquierda si es necesario
    return f"{codigo_otp:06d}"

# Ejemplo de uso
clave = "JBSWY3DPEHPK3PXP"  # Clave secreta de ejemplo (como las que usan apps 2FA)
print("Código 2FA:", generar_codigo_2fa(clave))