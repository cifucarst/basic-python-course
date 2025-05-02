import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8', errors='ignore')  # Convertimos de bytes a string
        s.close()
        return banner
    except Exception as e:
        return None


def checkVulns(banner):
    with open("vuln_banners.txt","r") as f:
        for line in f.readlines():
            if line.strip("\n") in banner:
                print(f"[+] Server is vulnerable: {banner.strip('\n')}")


def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(1, 255):
        ip = f'192.168.95.{x}'
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print(f'[+] {ip}:{port} → {banner.strip()}')
                checkVulns(banner)


if __name__ == '__main__':
    main()