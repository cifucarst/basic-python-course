# Ejercicio 4: Conversiones de Códigos de Estado HTTP
# 📌 Objetivo: Dado un diccionario con códigos de estado HTTP y su descripción, usa dictionary comprehension para categorizar los códigos en "Éxito" (2xx), "Redirección" (3xx) y "Error" (4xx, 5xx).

# 🔹 Instrucciones:
# Usa este diccionario base:

# codigos_http = {
#     200: "OK",
#     301: "Moved Permanently",
#     403: "Forbidden",
#     404: "Not Found",
#     500: "Internal Server Error"
# }
# Genera un nuevo diccionario donde el valor sea la categoría del código de estado (Éxito, Redirección, Error).

# 📌 Salida esperada:

# {
#     200: "Éxito",
#     301: "Redirección",
#     403: "Error",
#     404: "Error",
#     500: "Error"
# }


from typing import Dict

def categorizar_codigo_de_estado(codigos_http: Dict[int, str]) -> Dict[int, str]:
    """
    Devuelve un diccionario donde cada código HTTP está clasificado según su categoría.
    """
    if not isinstance(codigos_http, dict):
        raise ValueError("El parámetro codigos_http debe ser un diccionario con códigos HTTP y su descripción.")

    # Clasificación según los rangos oficiales de códigos HTTP
    categorias = {
        1: "Informativo",
        2: "Éxito",
        3: "Redirección",
        4: "Error del Cliente",
        5: "Error del Servidor"
    }

    return {codigo: categorias.get(codigo // 100, "Desconocido") for codigo in codigos_http}

# Diccionario de códigos HTTP
codigos_http = {
    200: "OK",
    301: "Moved Permanently",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}

# Clasificar los códigos y mostrar resultados
resultado = categorizar_codigo_de_estado(codigos_http)

print("\nCódigos HTTP categorizados:")
print("-" * 30)
for codigo, categoria in resultado.items():
    print(f"{codigo}: {categoria}")
