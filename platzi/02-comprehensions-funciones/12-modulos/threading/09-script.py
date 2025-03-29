import threading
import requests

urls = [
    "https://www.example.com/file1.jpg",
    "https://www.example.com/file2.jpg"
]

def descargar(url):
    response = requests.get(url)
    print(f"Descargado {url}, tamaño: {len(response.content)} bytes")

hilos = []
for url in urls:
    hilo = threading.Thread(target=descargar, args=(url,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todas las descargas han finalizado.")