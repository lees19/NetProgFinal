from socket import *
import threading
import hashlib

serverPort = 21
serverHost = ''
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(10)
print('The server is waiting on clients...')
workers = list()
requester = 0
passHash = 0

def requestHandler(passHash, solved):
    passHash = connectionSocket.recv(1024).decode()



def workerHandler(connectionSocket, workers, passHash):
    connectionSocket.send(passHash.encode())

while True:
     connectionSocket, addr = serverSocket.accept()

     print('Connection recieved from: ', addr)
     query = ("Welcome to the password cracker! Enter '1' to request a password to crack, or '2' to contribute to cracking a password.")
     
     connectionSocket.send(query.encode())
     queryResponse = connectionSocket.recv(1024).decode()

     if queryResponse == "1":
         if requester == 0:
             requestHandler(passHash, "no")
         else:
             connectionSocket.send("Currently handling a differnet request.".encode())
     elif queryResponse == "2":
         workerHandler(connectionSocket, workers, passHash)
         workers.append(connectionSocket)
         thread = threading.Thread(target=workerHandler, args=(connectionSocket, workers, passHash), daemon=True)
         thread.start()
     else:
         invalidMessage = ("Server did not recognize response.")
         connectionSocket.send(invalidMessage.encode())