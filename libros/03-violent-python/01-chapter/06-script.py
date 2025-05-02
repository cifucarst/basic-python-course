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
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('[+] FreeFloat FTP Server is vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('[+] 3CDaemon FTP Server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print('[+] Ability FTP Server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')


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