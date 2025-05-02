import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8', errors='ignore')  # decode necesario en Python 3
        s.close()
        return banner
    except socket.timeout:
        print(f"[-] Conexión a {ip}:{port} agotó el tiempo de espera.")
    except Exception as e:
        print(f"[-] Error al conectar con {ip}:{port} → {e}")
    return None


def main():
    targets = ['192.168.95.148', '192.168.95.149']
    port = 21

    for ip in targets:
        banner = retBanner(ip, port)
        if banner:
            print(f"[+] Banner recibido de {ip}:{port} → {banner.strip()}")
        else:
            print(f"[-] No se recibió banner de {ip}:{port}")


if __name__ == '__main__':
    main()
