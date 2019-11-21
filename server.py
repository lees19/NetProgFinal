from socket import *
import threading

serverPort = 21
serverHost = ''
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(10)
print('The server is waiting on clients...')
workers = list()

def requestHandler():
    pass

def workerHandler():
    pass

while True:
     connectionSocket, addr = serverSocket.accept()

     print('Connection recieved from: ', addr)
     query = ("Welcome to the password cracker! Enter '1' to request a password to crack, or '2' to contribute to cracking a password.")
     
     connectionSocket.send(query.encode())
     queryResponse = connectionSocket.recv(1024).decode()

     if queryResponse == "1":
         requestHandler()
     elif queryResponse == "2":
         workerHandler()
         workers.append(connectionSocket)
     else:
         invalidMessage = ("Server did not recognize response.")
         connectionSocket.send(invalidMessage.encode())