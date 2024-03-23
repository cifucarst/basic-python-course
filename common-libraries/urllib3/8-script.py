#!/usr/bin/env python3

import requests

# Disable insecure request warnings to prevent them from being shown
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Send a GET request to the specified URL with SSL verification disabled
# 'verify=False' indicates that SSL certificate verification is turned off
response = requests.get('https://13.109.185.30/', verify=False)

# Print the response text received from the server
print(response.text)