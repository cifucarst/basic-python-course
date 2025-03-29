# Ejercicio 1: Clasificación de Puertos
# 📌 Objetivo: Dado un diccionario con puertos y servicios, usa dictionary comprehension para clasificar los puertos en seguros (≤1024) e inseguros (>1024).

# 🔹 Instrucciones:
# Tienes el siguiente diccionario de puertos y servicios:

# puertos = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL", 8080: "HTTP-ALT"}
# Usa dictionary comprehension para generar un nuevo diccionario que clasifique los puertos así:

# {
#     22: "Seguro",
#     80: "Seguro",
#     443: "Seguro",
#     3306: "Inseguro",
#     8080: "Inseguro"
# }

puertos = {
    22: "SSH", 
    80: "HTTP", 
    443: "HTTPS", 
    3306: "MySQL", 
    8080: "HTTP-ALT"
}

clasificados = {puerto: "Seguro" if puerto <= 1024 else "Inseguro" for puerto in puertos}
print(clasificados)