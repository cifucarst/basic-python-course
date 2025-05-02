# ✅ Ejercicio 3: Detección de patrones maliciosos en logs con filter()
# 🕵️‍♂️ Contexto:
# Eres parte de un equipo Blue Team o estás haciendo análisis forense. Tienes acceso a los logs de peticiones HTTP de una aplicación web. Quieres detectar posibles ataques analizando el contenido de las URLs.

# 🧩 Instrucciones:
# Crea una función es_malicioso(url: str) -> bool que:

# Devuelva True si la URL contiene patrones sospechosos (como '--', ';', '<script>', ' OR ', etc.).

# Devuelva False en caso contrario.

# Usa filter() para obtener solo las URLs maliciosas desde un conjunto de logs.

# Imprime la lista de posibles ataques detectados.

# 🧪 Logs de ejemplo:

# logs_http = [
#     "/login?user=admin&pass=1234",
#     "/search?q=<script>alert(1)</script>",
#     "/product?id=10;DROP TABLE users",
#     "/home",
#     "/profile?id=1' OR '1'='1",
#     "/search?q=normal+query",
#     "/admin?user=admin' --"
# ]

# 💡 Tips:
# Puedes usar any() con una lista de patrones para hacer la detección de forma limpia.

# Esto es una forma sencilla de un WAF (Web Application Firewall) básico.

def es_malicioso(url: str) -> bool:
    if not isinstance(url, str):
        raise ValueError("La url debe estar en str")
    
    patrones = [
    "--", ";", "<script>", " or ", "' or '", "'='", 
    "'1'='1", "drop table", "select *", "<img", "onerror=", 
    "union select", "../", "%00"
    ]

    contiene_patrones_sospechosos = any(patron in url.lower() for patron in patrones)

    return True if contiene_patrones_sospechosos else False

logs_http = [
    "/login?user=admin&pass=1234",
    "/search?q=<script>alert(1)</script>",
    "/product?id=10;DROP TABLE users",
    "/home",
    "/profile?id=1' OR '1'='1",
    "/search?q=normal+query",
    "/admin?user=admin' --"
]

urls_maliciosas = list(filter(es_malicioso, logs_http))
print(urls_maliciosas)