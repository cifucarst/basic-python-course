import requests

url = "https://example.com/login"
data = {
    "username": "admin",
    "password": "password123"
}
response = requests.post(url, data=data)

print(f"Status Code: {response.status_code}")
print(f"Respuesta: {response.text[:500]}")