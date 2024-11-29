#!/usr/bin/env python3

import os

# Check if "14-regex.py" file exists
if os.path.exists("14-regex.py"):
    print(f"\n[+] The file '14-regex.py' exists")
else:
    print(f"\n[!] The file '14-regex.py' does not exist")

####################################################

# Check if "my_directory" directory exists, create if not
if not os.path.exists("my_directory"):
    os.mkdir("my_directory")
else:
    print(f"\n[!] The directory 'my_directory' already exists")

####################################################

# Check if "my_directory/my_subdirectory" directory exists, create if not
if not os.path.exists("my_directory/my_subdirectory"):
    os.makedirs("my_directory/my_subdirectory")
else:
    print(f"\n[!] The directory 'my_directory/my_subdirectory' already exists")

####################################################

# List all resources in the current working directory
print(f"\n[+] Listing all resources in the current working directory:")
resources = os.listdir()
for resource in resources:
    print(resource)

####################################################

# Check if "file1.txt" file exists, delete if so
if os.path.exists("file1.txt"):
    os.remove("file1.txt")

####################################################

# Check if "my_directory" directory exists, remove if so
if os.path.exists("my_directory"):
    os.rmdir("my_directory")

####################################################

# Check if "file2.txt" file exists, rename if so
if os.path.exists("file2.txt"):
    os.rename("file2.txt", "changed.txt")

####################################################

# Check if "/etc/passwd" file exists, get and print its size
if os.path.exists("/etc/passwd"):
    size = os.path.getsize("/etc/passwd")
    print(f"\n[+] The file '/etc/passwd' weighs {size} bytes")

####################################################

# Join directory and file name to create a path
path = os.path.join("my_directory", "my_file.txt")
print(f"\n[+] Path: {path}")

# Get the file name from the path
file_name = os.path.basename(path)
print(f"\n[+] File name: {file_name}")

# Get the directory name from the path
directory_name = os.path.dirname(path)
print(f"\n[+] Directory name where the file is contained: {directory_name}")
