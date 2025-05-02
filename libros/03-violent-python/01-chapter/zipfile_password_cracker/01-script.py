import zipfile
import argparse
from threading import Thread

def extract_file(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        print(f"[+] Found password: {password}\n")
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Zip file cracker using dictionary attack")
    parser.add_argument("-f", dest="zname", type=str, required=True, help="Specify zip file")
    parser.add_argument("-d", dest="dname", type=str, required=True, help="Specify dictionary file")
    args = parser.parse_args()

    zname = args.zname
    dname = args.dname

    try:
        zfile = zipfile.ZipFile(zname)
    except FileNotFoundError:
        print(f"[-] Zip file not found: {zname}")
        return
    except zipfile.BadZipFile:
        print(f"[-] Bad zip file format: {zname}")
        return

    try:
        with open(dname, 'r', encoding='utf-8', errors='ignore') as pass_file:
            for line in pass_file:
                password = line.strip()
                t = Thread(target=extract_file, args=(zfile, password))
                t.start()
    except FileNotFoundError:
        print(f"[-] Dictionary file not found: {dname}")

if __name__ == "__main__":
    main()