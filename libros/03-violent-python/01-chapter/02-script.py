import socket

# Establecer tiempo de espera predeterminado
socket.setdefaulttimeout(2)

# Crear socket TCP
s = socket.socket()

try:
    # Conectarse al servidor FTP en el puerto 21
    s.connect(("192.168.1.35", 21))
    # Recibir el banner (mensaje de bienvenida del servidor)
    ans = s.recv(1024).decode('utf-8', errors='ignore')  # decode requerido en Python 3
except Exception as e:
    print(f"[-] Error al conectar o recibir datos: {e}")
    s.close()
    exit()

# Comparar el banner con las cadenas conocidas de servidores vulnerables
if "FreeFloat Ftp Server (Version 1.00)" in ans:
    print("[+] FreeFloat FTP Server is vulnerable.")
elif "3Com 3CDaemon FTP Server Version 2.0" in ans:
    print("[+] 3CDaemon FTP Server is vulnerable.")
elif "Ability Server 2.34" in ans:
    print("[+] Ability FTP Server is vulnerable.")
elif "Sami FTP Server 2.0.2" in ans:
    print("[+] Sami FTP Server is vulnerable.")
else:
    print("[-] FTP Server is not vulnerable.")

# Cerrar la conexión
s.close()
