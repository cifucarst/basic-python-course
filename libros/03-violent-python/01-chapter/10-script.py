import socket
import os
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8', errors='ignore')
        s.close()
        return banner
    except:
        return None


def checkVulns(banner, filename):
    with open(filename, 'r') as f:
        for line in f:
            if line.strip() in banner:
                print(f'[+] Server is vulnerable: {banner.strip()}')


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        if not os.path.isfile(filename):
            print(f'[-] {filename} does not exist.')
            sys.exit(0)

        if not os.access(filename, os.R_OK):
            print(f'[-] {filename} access denied.')
            sys.exit(0)
    else:
        print(f'[-] Usage: {sys.argv[0]} <vuln filename>')
        sys.exit(0)

    portList = [21, 22, 25, 80, 110, 443]
    for x in range(147, 150):  # Cambia esto según tu red
        ip = f'192.168.95.{x}'
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print(f'[+] {ip}:{port} → {banner.strip()}')
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()