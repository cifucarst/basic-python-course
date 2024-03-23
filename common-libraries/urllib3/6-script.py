#!/usr/bin/env python3

import urllib3

# Import the required libraries
http = urllib3.PoolManager()

# Send a GET request to the specified URL without following redirects
response = http.request(
    'GET',
    'https://httpbin.org/redirect/1',
    redirect=False
)

# Print the information about the redirection, including the status code and the redirect location if applicable
print(f"\n[+] The path we're being redirected to with the status code {response.status} is: {response.get_redirect_location()}")