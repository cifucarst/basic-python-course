#!/usr/bin/env python3

import shutil
import os

# Check if "my_directory" directory exists, remove it if so
if os.path.exists("my_directory"):
    shutil.rmtree("my_directory")

# Create a new directory "new_directory"
os.mkdir("new_directory")

# Copy a file "example.txt" to the new directory
shutil.copy("example.txt", "new_directory")

# Print a message indicating the completion of the operations
print("\n[+] Operations completed successfully.")