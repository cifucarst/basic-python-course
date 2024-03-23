#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining the URL to send the GET request to
url = 'http://github.com'

# Sending a GET request to the specified URL
r = requests.get(url)

# Iterating over the history of redirections (if any) made during the request
for request in r.history:
    # Printing the URL and status code of each intermediate redirection
    print(f"\n[+] Passed through the domain {request.url} with a status code {request.status_code}")

# Printing the final URL and status code after all redirections (if any)
print(f"\n[+] Final URL: {r.url} with a status code {r.status_code}")