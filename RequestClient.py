from socket import*
import hashlib

socket = socket(AF_INET, SOCK_STREAM)
serverName = 'localhost'
port = 21
socket.connect((serverName, port))
socket.send("1".encode())
pswdHash = input('Enter the hash you want to crack (Six Character Max): ')
pswdHash = hashlib.md5(pswdHash.encode())
socket.send(pswdHash.hexdigest().encode())

print('File delivered to server.')
print('receiving data...\n')

while True:
         data = socket.recv(1024)
         if len(data) != 0:
                 print(data.decode())
print('\nFile succesfully recieved')