#!/usr/bin/env python3

# Importing necessary modules from requests library
from requests import Request, Session

# Defining the URL for the GET request
url = 'https://httpbin.org/get'

# Creating a Session object to manage the request
s = Session()

# Defining custom headers to be included in the request
headers = {'Custom-Header': 'my_custom_header'}

# Creating a Request object with specified method, URL, and headers
req = Request('GET', url, headers=headers)

# Preparing the request before sending
prepped = req.prepare()

# Modifying the headers of the prepared request
prepped.headers['Custom-Header'] = 'my_header_chaged'
prepped.headers['Another-Header'] = 'this_is_another_header'

# Sending the modified request using the Session object
response = s.send(prepped)

# Printing the response content received from the server
print(response.text)