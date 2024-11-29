#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

try: 
    # Sending a GET request to the specified URL with a timeout of 1 second
    response = requests.get('https://google.ese', timeout=1)
    
    # Checking for any HTTP errors in the response
    response.raise_for_status()
except requests.Timeout:
    # Handling timeout error if the request exceeds the specified timeout duration
    print(f"\n[!] The request has exceeded the timeout limit")
except requests.HTTPError as http_err:
    # Handling HTTP errors such as 404, 500, etc.
    print(f"\n[!] HTTP Error: {http_err}")
except requests.RequestException as err:
    # Handling other types of request exceptions
    print(f"\n[!] Error: {err}")
else:
    # Printing a message indicating that no errors occurred during the request
    print(f"\n[+] There have been no errors in the request")