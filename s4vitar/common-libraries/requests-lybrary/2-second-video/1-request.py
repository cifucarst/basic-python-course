#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Sending a GET request to the specified URL with basic authentication credentials
# The username is "foo" and the password is "bar"
response = requests.get("https://httpbin.org/basic-auth/foo/bar", auth=("foo", "bar"))

# Printing the response content received from the server
print(response.text)