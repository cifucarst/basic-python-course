#!/usr/bin/env python3

import requests
import threading
import time

# Function to make HTTP GET requests to the provided URL
def make_request(url):
    response = requests.get(url)
    # Print the URL and the size of the response content in bytes
    print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

# List of domains to send requests to
domains = [
    "https://google.com",
    "https://xvideos.com",
    "https://yahoo.com",
    "https://wikipedia.org",
]

# Record the start time of the request processing
start_time = time.time()

# Create a list to store the threads
threads = []
# Iterate over each domain in the list
for url in domains:
    # Create a new thread for each domain, specifying the target function and its arguments
    thread = threading.Thread(target=make_request, args=(url,))
    # Start the thread
    thread.start()
    # Add the thread to the list of threads
    threads.append(thread)

# Wait for each thread to complete before continuing
for thread in threads:
    thread.join()

# Record the end time of the request processing
end_time = time.time()

# Print the total time elapsed for all requests to complete
print(f"\n[+] Total time elapsed: {round(end_time - start_time, 2)} seconds")