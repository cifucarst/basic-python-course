import socket
import threading

class FastPortScanner:
    def __init__(self, ip, ports, timeout=0.5):
        self.ip = ip
        self.ports = ports
        self.timeout = timeout
        self.open_ports = 0
        self.closed_ports = 0

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.ip, port))
                if result == 0:
                    print(f"✅ Puerto {port} abierto")
                    self.open_ports += 1
                else:
                    self.closed_ports += 1
        except Exception as e:
            print(f"❌ Error en puerto {port}: {e}")

    def scan_ports(self):
        threads = []

        for port in self.ports:
            t = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def __str__(self):
        return (f"\nEscaneo completo:\n"
                f"IP escaneada: {self.ip}\n"
                f"Puertos escaneados: {len(self.ports)}\n"
                f"Puertos abiertos: {self.open_ports}\n"
                f"Puertos cerrados: {self.closed_ports}")

if __name__ == '__main__':
    scanner = FastPortScanner('127.0.0.1', range(1, 1024))
    scanner.scan_ports()
    print(scanner)