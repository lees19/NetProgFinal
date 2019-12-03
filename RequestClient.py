from socket import*
import hashlib
import time
import re

# Sets up connection with server
socket = socket(AF_INET, SOCK_STREAM)
serverName = 'localhost'
port = 21
socket.connect((serverName, port))

# Sends requester identififier to server and gets a password to crack from the user
socket.send("1".encode())
while True:
    pswdHash = input('Enter the hash you want to crack (Six character max, no special characters): ')
    if re.match("^[a-zA-Z0-9_]*$", pswdHash) and len(pswdHash) < 6 and len(pswdHash) >= 1:
        pswdHash = hashlib.md5(pswdHash.encode())
        socket.send(pswdHash.hexdigest().encode())
        break
    else:
        print('Password did not fit parameters.')
print('File delivered to server.')
print('Waiting on response...\n')

# Waits on response from the server
while True:
    data = socket.recv(1024)
    if len(data) != 0:
        print(data.decode())
        print("Program will automatically close in ten seconds.")
        time.sleep(10)
        exit()