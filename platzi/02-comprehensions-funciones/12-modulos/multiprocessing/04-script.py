import multiprocessing
import socket

def scan_port(target_ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[*] Puerto {port} abierto")

if __name__ == "__main__":
    target = "scanme.nmap.org"  # Prueba con un host accesible
    ports = range(1, 1025)

    with multiprocessing.Pool(processes=10) as pool:
        pool.starmap(scan_port, [(target, port) for port in ports])