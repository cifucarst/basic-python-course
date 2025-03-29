import requests

session = requests.Session()

login_url = "https://example.com/login"
data = {"username": "admin", "password": "password123"}

# Autenticarse
session.post(login_url, data=data)

# Acceder a una página protegida
protected_url = "https://example.com/dashboard"
response = session.get(protected_url)

print(response.text)