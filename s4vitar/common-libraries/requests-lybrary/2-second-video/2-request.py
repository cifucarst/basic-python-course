#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests
# Importing HTTPBasicAuth from requests.auth module to use HTTP Basic Authentication
from requests.auth import HTTPBasicAuth

# Sending a GET request to the specified URL with HTTP Basic Authentication
# The username is "foo" and the password is "bar"
response = requests.get("https://httpbin.org/basic-auth/foo/bar", auth=HTTPBasicAuth("foo", "bar"))

# Printing the response content received from the server
print(response.text)
