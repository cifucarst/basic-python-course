#!/usr/bin/env python3

import requests
import threading
import time

dominios = [
    "https://google.com",
    "https://xvideos.com",
    "https://yahoo.com",
    "https://wikipedia.org",
]

start_time = time.time()

for url in dominios:
    response = requests.get(url)
    print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

end_time = time.time()

print(f"\n[+] Tiempo total transcurrido: {end_time - start_time} segundos")