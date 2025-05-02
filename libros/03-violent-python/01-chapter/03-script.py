import socket

socket.setdefaulttimeout(2)

s = socket.socket()

try:
    s.connect(("192.168.95.149", 21))
except Exception as e:
    print(f"[-] Error = {e}")


# [-] Error = Operation timed out