import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8', errors='ignore')  # Decodificamos los bytes a str
        s.close()
        return banner
    except Exception as e:
        print(f"[-] Error conectando a {ip}:{port} → {e}")
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
    ip_list = ['192.168.95.148', '192.168.95.149', '192.168.95.150']
    port = 21

    for ip in ip_list:
        banner = retBanner(ip, port)
        if banner:
            print(f'[+] {ip} : {banner.strip()}')
            checkVulns(banner)


if __name__ == '__main__':
    main()