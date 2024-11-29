#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining cookies to be sent with the request
cookies = dict(cookies_are='working')

# Sending a GET request to the specified URL with the defined cookies
response = requests.get('https://httpbin.org/cookies', cookies=cookies)

# Printing the response content received from the server
print(response.text)