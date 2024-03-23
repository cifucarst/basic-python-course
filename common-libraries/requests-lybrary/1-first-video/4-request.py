#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining custom headers for the request, in this case, specifying the User-Agent
headers = {'User-Agent': 'cualquier cosa'}

# Sending a GET request to the specified URL with custom headers
response = requests.get("https://google.com", headers=headers)

# Printing the headers sent in the request
print(response.request.headers)
