#!/usr/bin/env python3

import urllib3
import json

http = urllib3.PoolManager()

data = {'atributo':'value'}
encoded_data = json.dumps(data).encode()

response = http.request('POST','https://httpbin.org/post', body=encoded_data, headers= {'Content-Type': 'application/json'})

print(response.data.decode())