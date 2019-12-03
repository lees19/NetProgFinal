from socket import *
import threading
import hashlib
import time

serverPort = 21
serverHost = ''
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(10)
print('The server is waiting on clients...')
workers = list()
workerHandlers = list()
requesters = list()
requester = 0
passHash = ""
hashs = list()
hashs.append(passHash)

def requestHandler(solved):
    global passHash
    passHash = (connectionSocket.recv(1024).decode())
    print(passHash)
    while True:
        print(2)
        time.sleep(3)

def workerHandler(connectionSocket, workers, requesters):
    global passHash
    while True:
        print(1)
        time.sleep(3)
        sendHash = ""
        if len(requesters) == 1:
            if passHash is not "":
                sendHash = passHash
                connectionSocket.send(sendHash.encode())
            if len(workers) == 1:
                parameters = "123456"
                workers[0].send(parameters.encode())
                if sendHash != "":
                    break
            elif len(workers) == 2:
                parameters = "16"
                workers[0].send(parameters.encode())
                parameters = "2345"
                workers[1].send(parameters.encode())
            elif len(workers) == 3:
                parameters = "6"
                workers[0].send(parameters.encode())
                parameters = "15"
                workers[1].send(parameters.encode())
                parameters = "234"
                workers[2].send(parameters.encode())
            elif len(workers) == 4:
                parameters = "6"
                workers[0].send(parameters.encode())
                parameters = "5"
                workers[1].send(parameters.encode())
                parameters = "14"
                workers[2].send(parameters.encode())
                parameters = "23"
                workers[3].send(parameters.encode())
            elif len(workers) == 5:
                parameters = "6"
                workers[0].send(parameters.encode())
                parameters = "5"
                workers[1].send(parameters.encode())
                parameters = "4"
                workers[2].send(parameters.encode())
                parameters = "3"
                workers[3].send(parameters.encode())
                parameters = "12"
                workers[4].send(parameters.encode())
            elif len(workers) == 6:
                parameters = "6"
                workers[0].send(parameters.encode())
                parameters = "5"
                workers[1].send(parameters.encode())
                parameters = "4"
                workers[2].send(parameters.encode())
                parameters = "3"
                workers[3].send(parameters.encode())
                parameters = "2"
                workers[4].send(parameters.encode())
                parameters = "1"
                workers[6].send(parameters.encode())
    response = connectionSocket.recv(1024).decode()
    if len(response) != 0:
        print(response)
        if response == 'Failure to find password.':
            print (addr + 'Did not find the password.')
            connectionSocket.close()
        else:
            print('Password found! ' + response)
            requesters[0].send(response.encode())
                        
while True:
     connectionSocket, addr = serverSocket.accept()

     print('Connection recieved from: ', addr)
     queryResponse = connectionSocket.recv(1024).decode()

     if queryResponse == "1":
         if len(requesters) == 0:
             print(addr, " Is a requester.")
             requester = 1      
             reqThread = threading.Thread(target= requestHandler, args=("no",), daemon=True)
             reqThread.start()
             requesters.append(reqThread)
             
         else:
             connectionSocket.send("Currently handling a differnet request.".encode())
             connectionSocket.close()
     elif queryResponse == "2":
         if len(workers) == 6:
             maxMessage = "Number of workers at capacity."
             connectionSocket.send(maxMessage.encode())
             connectionSocket.close()
         else: 
             print(addr, " Is a worker.")
             workers.append(connectionSocket)
             workThread = threading.Thread(target=workerHandler, args=(connectionSocket, workers, requesters,), daemon=True)
             workerHandlers.append(workThread)
             workThread.start()
 
     else:
         invalidMessage = ("Server did not recognize response.")
         connectionSocket.send(invalidMessage.encode())