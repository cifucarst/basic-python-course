#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining a dictionary containing key-value pairs for form data
payload = {'key':'value','key1':'value1','key2':'value2'}

# Sending a POST request to the specified URL with the defined form data
response = requests.post("https://httpbin.org/post",data=payload)

# Printing the content of the response received from the server
print(f"\n[+] Content: {response.text}")