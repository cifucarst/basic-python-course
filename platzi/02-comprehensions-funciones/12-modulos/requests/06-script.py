import requests

proxies = {
    "http": "http://127.0.0.1:8080",  # Proxy BurpSuite
    "https": "http://127.0.0.1:8080"
}

url = "https://example.com"
response = requests.get(url, proxies=proxies)

print(response.text)
