# 1. Importar y Usar el Módulo
# El módulo nmap permite interactuar con Nmap mediante la clase principal nmap.PortScanner.

# Creación del objeto PortScanner


import nmap

# Crear una instancia del escáner
scanner = nmap.PortScanner()
print(dir(scanner))