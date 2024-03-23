#!/usr/bin/env python3

import urllib3
import json

# Import the required libraries
http = urllib3.PoolManager()

# Define a dictionary containing data with a key 'attribute' and its corresponding value 'value'
data = {'attribute': 'value'}

# Encode the data dictionary into JSON format and then encode it into bytes format
encoded_data = json.dumps(data).encode()

# Send a POST request to the specified URL with the encoded data as the request body
response = http.request('POST', 'https://httpbin.org/post', body=encoded_data)

# Decode and print the response data received from the server
print(response.data.decode())