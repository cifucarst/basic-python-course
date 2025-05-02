import hashlib

def hash_password_sha512(password):
    """Hash a password using SHA-512"""
    return hashlib.sha512(password.encode()).hexdigest()


def testPass(cryptPass):
    try:
        with open('dictionary.txt', 'r') as dictFile:
            for word in dictFile:
                word = word.strip()
                hashedWord = hash_password_sha512(word)
                if hashedWord == cryptPass:
                    print(f"[+] Found Password: {word}\n")
                    return
    except FileNotFoundError:
        print("[-] dictionary.txt not found.")
        return

    print("[-] Password Not Found.\n")


def main():
    try:
        with open('passwords_sha512.txt', 'r') as passFile:
            for line in passFile:
                if ":" in line:
                    user = line.split(':')[0]
                    cryptPass = line.split(':')[1].strip()
                    print(f"[*] Cracking Password For: {user}")
                    testPass(cryptPass)
    except FileNotFoundError:
        print("[-] passwords_sha512.txt not found.")


if __name__ == "__main__":
    main()