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

for url in logs_http:
    if es_malicioso(url):
        print(f"[ALERTA] Posible ataque en: {url}")