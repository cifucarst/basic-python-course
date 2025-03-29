import requests
import socket

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

url = "http://check.torproject.org"  # Página que verifica si usamos Tor
response = requests.get(url, proxies=proxies)

print(response.text)
