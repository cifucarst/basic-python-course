#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining a dictionary containing key-value pairs for query parameters
values = {'key1': 'value1','key2':'value2','key3':'value3'}

# Sending a GET request to the specified URL with the defined query parameters
response = requests.get("https://httpbin.org/get", params=values)

# Printing the final URL with query parameters after encoding
print(f"\n[+] Final URL: {response.url}\n")

# Printing the response content received from the server
print(f"Response:\n{response.text}")