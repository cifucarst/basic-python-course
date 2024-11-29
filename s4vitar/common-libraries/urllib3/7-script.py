#!/usr/bin/env python3

import urllib3

# Disable insecure platform warnings to prevent them from being shown
urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)

# Create a PoolManager object from the urllib3 library with certificate verification disabled
# This allows requests to servers with invalid or self-signed certificates
http = urllib3.PoolManager(cert_reqs='CERT_NONE')

# Send a GET request to the specified URL using the PoolManager object
response = http.request('GET','https://13.109.185.30/')

# Decode and print the response data received from the server
print(response.data.decode())