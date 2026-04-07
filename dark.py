import socket
import sys
print ("ENTER THE URL OF YOUR TARGET: ")
URL = input()
ip = socket.gethostbyname(URL)
print ("HOST URL: ",URL,'\n',"TARGET IP: ",ip)
