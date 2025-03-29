import requests

xss_url = "https://example.com/search"
payload = {"q": "<script>alert('XSS')</script>"}

response = requests.get(xss_url, params=payload)

if "<script>alert('XSS')</script>" in response.text:
    print("¡Posible XSS detectado!")