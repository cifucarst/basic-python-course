import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]

    if not os.path.isfile(filename):
        print(f'[-] {filename} does not exist.')
        sys.exit(0)

    if not os.access(filename, os.R_OK):
        print(f'[-] {filename} access denied.')
        sys.exit(0)

    print(f'[+] Reading Vulnerabilities From: {filename}')
else:
    print(f'Usage: {sys.argv[0]} <filename>')
    sys.exit(0)