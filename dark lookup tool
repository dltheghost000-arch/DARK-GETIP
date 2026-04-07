# اسم الملف: dns_lookup.py
import socket
import sys

def main():
    print("ENTER THE URL OF YOUR TARGET: ")
    URL = input()
    try:
        ip = socket.gethostbyname(URL)
        print("HOST URL: ", URL)
        print("TARGET IP: ", ip)
    except socket.gaierror:
        print("Invalid URL or unable to resolve hostname")

if __name__ == "__main__":
    main()
