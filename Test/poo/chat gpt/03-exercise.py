# 3. **Dispositivo de red**
#    Clase `Dispositivo` con atributos: `ip`, `mac`, `estado`.

#    * Método para encender/apagar el dispositivo.
#    * Método para mostrar la información en formato tipo Nmap: `"IP: 192.168.0.1 - MAC: AA:BB:CC:DD - Estado: Activo"`.

import ipaddress
import re

class Dispositivo:
    def __init__(self, ip: str, mac: str, estado: str):

        if not ip or not isinstance(ip, str):
            raise ValueError("La ip no debe estar vacia")
        if not self._validar_ip(ip):
            raise ValueError("ip inválida")
        if not self._validar_mac(mac):
            raise ValueError("mac inválida")
        
        self.ip = ip
        self.mac = mac
        self.estado = estado

    def encender_dispositivo(self):
        if self.estado.capitalize() == "Activo":
            print(f"Ya esta encendido el dispositivo")
        elif self.estado.capitalize() == "Inactivo":
            self.estado = "Activo"
            print(f"Dispositivo encendido")
        else:
            print("No se reconoce el estado")

    def _validar_ip(self, ip: str):
        # patron1 = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        patron2 = r'^(\d{1,3}\.){1,3}\d{1,3}$'
        return bool(re.match(patron2, ip))
    
    def _validar_mac(self, mac: str):
        patron = r'^$'
        return bool(re.match(patron, mac))

    def __str__(self):
        # IP: 192.168.0.1 - MAC: AA:BB:CC:DD - Estado: Activo
        return f"IP: {self.ip} - MAC: {self.mac} - Estado: {self.estado}"


def solicitar_info():
    ip = input("Ingresa una direccion ip (192.168.0.1) ").strip().lower()
    mac = input("Ingresa una mac address (AA:BB:CC:DD) ").strip().upper()
    estado = input("Ingresa el estado del dispositivo (activo o inactivo) ").strip().capitalize()
    return ip, mac,estado

try:
    ip, mac, estado = solicitar_info()
    dispositivo1 = Dispositivo(ip, mac, estado)
    print(dispositivo1)
    dispositivo1.encender_dispositivo()
    print(dispositivo1)
except ValueError as err:
    print(f"Ha ocurrido un error: {err}")

# print(dir(ipaddress))
# print(help(ipaddress))

# Aprender modulo ipaddress para crear las verificaciones