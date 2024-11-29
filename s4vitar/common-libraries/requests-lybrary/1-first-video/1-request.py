#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Sending a GET request to the specified URL
response = requests.get("https://google.com")

# Printing the status code of the response
print(f"\n[+] Status code: {response.status_code}")

# Informing the user about saving the response code into a file
print(f"\n[+] Saving the response code into a file named index.html\n")

# Opening a file named index.html in write mode and saving the response content into it
with open("index.html","w") as f:
    f.write(response.text)