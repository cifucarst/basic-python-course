#!/usr/bin/env python3

import urllib3
import json

# Import the required libraries
http = urllib3.PoolManager()

# Send a GET request to the specified URL with a custom header 'nuevaCabecera' and its value 'cualquier cosa'
response = http.request('GET', 'https://httpbin.org/get', headers={'newHeader': 'anything'})

# Decode and print the response data received from the server
print(response.data.decode())