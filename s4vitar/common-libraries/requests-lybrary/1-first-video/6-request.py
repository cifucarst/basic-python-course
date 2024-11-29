#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Sending a GET request to the specified URL
response = requests.get("https://httpbin.org/get")

# Parsing the response content as JSON
data = response.json()

# Checking if the 'headers' field exists in the response and if it contains the 'User-Agent' field
if 'headers' in data and 'User-Agent' in data['headers']:
    # Extracting the User-Agent value from the response
    user_agent = data['headers']['User-Agent']
    # Printing the User-Agent value
    print(f"\n[+] User-Agent: {user_agent}")
else:
    # Printing a message indicating that the specified field does not exist in the response
    print(f"\n[!] The specified field does not exist in the response")
