from typing import List, Tuple

def extract_open_ports(scan_results: List[Tuple[int, str]]) -> List[int]:
    """Extrae los números de los puertos que están abiertos."""
    return [port for port, status in scan_results if status == "open"]

# Datos de escaneo
scan_results = [
    (22, "open"), (80, "closed"), (443, "open"),
    (3306, "filtered"), (8080, "open")
]

# Imprimir resultado
print(extract_open_ports(scan_results))