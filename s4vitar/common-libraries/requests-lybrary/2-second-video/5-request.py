#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining the URLs for the main page and the URL to set cookies
url = "https://httpbin.org/cookies"
set_cookies_url = "https://httpbin.org/cookies/set/my_cookie/123123"

# Creating a session object to persist cookies across requests
s = requests.Session()

# Sending a GET request to set the specified cookies
response = s.get(set_cookies_url)

# Sending a GET request to the main URL with the session object, 
# which contains the cookies set in the previous request
response = s.get(url)

# Printing the response content received from the server
print(response.text)