#!/usr/bin/env python3

import sys

print(f"\n[+] Script name: {sys.argv[0]}")

print(f"\n[+] Total number of arguments passed to the program: {len(sys.argv)}")

print(f"\n[+] Displaying the first argument: {sys.argv[1]}")  # python3 2-sys.py test

print(f"\n[+] Displaying the second argument: {sys.argv[2]}")

print(f"\n[+] Displaying all arguments: {','.join(argument for argument in sys.argv)}")

print("\n[+] Displaying Python paths:\n")

for element in sys.path:
    print(element)