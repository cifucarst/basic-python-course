import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://example.com",
    "Cookie": "sessionid=1234567890",
    "X-Forwarded-For": "192.168.1.100"  # Para suplantar IP
}

url = "https://example.com/profile"
response = requests.get(url, headers=headers)

print(response.text)