#!/usr/bin/env python3

import urllib3

# Import the urllib3 library for making HTTP requests
http = urllib3.PoolManager()

# Define the data to be sent in the POST request
data = "This is a little test"

# Encode the data into bytes format as required by HTTP POST requests
encoded_data = data.encode()

# Send a POST request to the specified URL with the encoded data
response = http.request('POST','https://httpbin.org/post', body=encoded_data)

# Decode and print the response data received from the server
print(response.data.decode())