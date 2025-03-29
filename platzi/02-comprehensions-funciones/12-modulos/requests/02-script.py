import requests

url = "https://example.com"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Contenido: {response.text[:500]}")  # Muestra solo los primeros 500 caracteres