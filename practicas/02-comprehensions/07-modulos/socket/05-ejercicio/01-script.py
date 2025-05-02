import socket
import ipaddress


class PortScanner:
    def __init__(self, ip: str, ports: list):
        self.ip = ip
        self.ports = ports
        self.open_ports = 0
        self.closed_ports = 0

    def scan_ports(self):
        for port in self.ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex((self.ip, port))
                    if result == 0:
                        print(f"✅ Puerto {port} abierto")
                        self.open_ports += 1
                    else:
                        self.closed_ports += 1
            except Exception as e:
                print(f"❌ Ha ocurrido un error: {e}")

    def __str__(self):
        return f"\n[+] Dirección ip escaneada: {self.ip}\nPuertos escaneados: {len(self.ports)}\nPuertos abiertos: {self.open_ports}\nPuertos Cerrados: {self.closed_ports}"


class PersonalizedPortScanner(PortScanner):
    def __init__(self, ip, ports, timeout):
        super().__init__(ip, ports)
        self.timeout = timeout

    def ask_info(self):
        while True:
            try:
                self.ip = input("Escribe la dirección IP a escanear: ")
                ipaddress.ip_address(self.ip)  # Esto validará si la IP tiene un formato correcto
                break
            except ValueError:
                print("❌ Error: La dirección IP ingresada no es válida. Por favor, inténtalo de nuevo.")

        while True:
            try:
                self.timeout = float(input("Escribe el tiempo de espera en cada puerto (en segundos): "))
                if self.timeout <= 0:
                    raise ValueError
                break
            except ValueError:
                print("❌ Error: El tiempo de espera debe ser un número positivo. Por favor, inténtalo de nuevo.")

        while True:
            self.ports_input = input("Escribe el rango de puertos a escanear o el puerto a escanear (ejem. 1-1024 o 80): ")
            if '-' in self.ports_input:
                try:
                    start_port, end_port = map(int, self.ports_input.split('-'))
                    if 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port:
                        self.ports = list(range(start_port, end_port + 1))  # Convertir a lista
                        break
                    else:
                        print("❌ Error: El rango de puertos debe estar entre 1 y 65535, y el puerto de inicio debe ser menor o igual al puerto de fin. Por favor, inténtalo de nuevo.")
                except ValueError:
                    print("❌ Error: El formato del rango de puertos es incorrecto. Por favor, usa el formato 'inicio-fin' (ejem. 1-1024).")
            else:
                try:
                    port = int(self.ports_input)
                    if 1 <= port <= 65535:
                        self.ports = [port]
                        break
                    else:
                        print("❌ Error: El puerto debe estar entre 1 y 65535. Por favor, inténtalo de nuevo.")
                except ValueError:
                    print("❌ Error: El valor ingresado para el puerto no es un número válido. Por favor, inténtalo de nuevo.")

        return self.ip, self.ports, self.timeout

    def scan_ports(self):
        ip, ports, timeout = self.ask_info()
        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(timeout)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        print(f"✅ Puerto {port} abierto")
                        self.open_ports += 1
                    else:
                        print(f"❌ Puerto {port} cerrado")
                        self.closed_ports += 1
            except Exception as e:
                print(f"❌ Ha ocurrido un error: {e}")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nTiempo de espera: {self.timeout} segundos"


if __name__ == '__main__':
    personalized = int(input("¿Quieres personalizar el escaneo? (1 = Normal, 2 = Personalizado): "))

    if personalized == 1:
        scanner = PortScanner('127.0.0.1', list(range(1, 1024)))
        scanner.scan_ports()
        print(scanner)
    elif personalized == 2:
        better_scanner = PersonalizedPortScanner('127.0.0.1', list(range(1, 1024)), 0.5)
        better_scanner.scan_ports()
        print(better_scanner)
    else:
        print("❌ Elegiste una opción incorrecta, debes presionar 1 o 2.")