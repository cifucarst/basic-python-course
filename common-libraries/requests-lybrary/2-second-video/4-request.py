#!/usr/bin/env python3

# Importing the requests module to handle HTTP requests
import requests

# Defining the URL to send the POST request to
url = "https://httpbin.org/post"

# Creating a dictionary containing the file to be uploaded with the key 'archivo'
# 'example.txt' is opened in read mode ('r')
my_file = {'archivo': open('example.txt', 'r')}

# Sending a POST request to the specified URL with the defined file
response = requests.post(url, files=my_file)

# Printing the response content received from the server
print(response.text)