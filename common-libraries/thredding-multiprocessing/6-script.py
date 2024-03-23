#!/usr/bin/env python3

import requests
import multiprocessing
import time

# Function to make HTTP GET requests to the provided URL
def make_request(url):
    response = requests.get(url)
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

# Create a list to store the processes
processes = []
# Iterate over each domain in the list
for url in domains:
    # Create a new process for each domain, specifying the target function and its arguments
    process = multiprocessing.Process(target=make_request, args=(url,))
    # Start the process
    process.start()
    # Add the process to the list of processes
    processes.append(process)

# Wait for each process to complete before continuing
for pro in processes:
    pro.join()

# Record the end time of the request processing
end_time = time.time()

# Print the total time elapsed for all requests to complete
print(f"\n[+] Total time: {round(end_time - start_time,2)} seconds")