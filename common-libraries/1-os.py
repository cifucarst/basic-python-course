#!/usr/bin/env python3

import os

# Get the absolute path of the current directory
current_directory = os.getcwd()

print(f"\n[+] Current working directory: {current_directory}")

# List files in the current directory
files = os.listdir(current_directory)
print(files)
print(type(files))

print(f"\n[+] Listing existing files in directory {current_directory}:")
for file in files:
    print(file)

# Create a directory
if not os.path.exists("my_directory"):
    os.mkdir("my_directory")

    # List files after directory creation
    files = os.listdir(current_directory)

    print(f"\n[+] Directory 'my_directory' created:\n")
    for file in files:
        print(file)

# Check if a file exists
print(f"\n[+] Does 'my_file.txt' exist? -> {os.path.exists('my_file.txt')} ")

# Get environment variables
value = os.getenv('XAUTHORITY')

print(f"\n[+] Value of the 'XAUTHORITY' environment variable: {value}")