import socket


socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.1.1",21))
ans = s.recv(1024)
print(ans)


# 220 FreeFloat Ftp Server (Version 1.00).