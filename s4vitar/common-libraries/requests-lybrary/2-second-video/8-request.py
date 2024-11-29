#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Using a session to persist parameters across requests
with requests.Session() as session:
    # Setting up basic authentication credentials for the session
    session.auth = ('foo', 'bar')
    
    # Sending a GET request to a URL requiring basic authentication
    response1 = session.get('https://httpbin.org/basic-auth/foo/bar')
    # Printing the response content from the first request
    print(response1.text)

    # Sending another GET request to the same URL with the same session
    response2 = session.get('https://httpbin.org/basic-auth/foo/bar')
    # Printing the response content from the second request
    print(response2.text)