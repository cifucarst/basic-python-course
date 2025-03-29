# Ejercicio 2: Extraer puertos abiertos en un escaneo
# Dada una lista de respuestas de un escaneo de puertos, usa list comprehension para extraer los números de los puertos abiertos ("open").


# scan_results = [
#     (22, "open"), (80, "closed"), (443, "open"),
#     (3306, "filtered"), (8080, "open")
# ]

def extract_open_ports(scan_results):
    return [i[0] for i in scan_results if i[1] == "open"]


scan_results = [
    (22, "open"), (80, "closed"), (443, "open"),
    (3306, "filtered"), (8080, "open")
]

print(extract_open_ports(scan_results))