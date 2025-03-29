import multiprocessing
import scapy.all as scapy
import ipaddress
import netifaces

def get_local_network():
    """ Obtiene la dirección IP de la interfaz de red y la convierte en un rango de IPs """
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]  # Obtiene la interfaz activa
    ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    
    local_ip = ip_info['addr']  # Dirección IP local
    subnet_mask = ip_info['netmask']  # Máscara de subred
    
    network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict=False)
    return network

def arp_scan(ip):
    """ Envía una solicitud ARP y verifica si hay respuesta """
    arp_request = scapy.ARP(pdst=str(ip))
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    response = scapy.srp(packet, timeout=1, verbose=False)[0]

    for sent, received in response:
        print(f"[+] Dispositivo encontrado: {received.psrc} - {received.hwsrc}")

if __name__ == "__main__":
    network = get_local_network()
    
    print(f"Escaneando red: {network}")
    
    with multiprocessing.Pool(processes=10) as pool:
        pool.map(arp_scan, [ip for ip in network.hosts()])
    
    print("Escaneo finalizado.")