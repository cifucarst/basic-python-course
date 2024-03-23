#!/usr/bin/env python3

import urllib3

# Create a PoolManager object from the urllib3 library to manage HTTP connections
http = urllib3.PoolManager() 

# Send a GET request to the specified URL using the PoolManager object
response = http.request('GET', 'https://httpbin.org/get')

# Decode and print the response data received from the server
print(response.data.decode())