from socket import *
import threading
import hashlib
import time
import sys
import os

# Initializing global variables and setting up connection socket
serverPort = 21
serverHost = ''
serverSocket = socket(AF_INET, SOCK_STREAM)
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

# Handles requesting client, assigning the passHash variable and printing it out
def requestHandler(solved):
    global passHash
    passHash = (connectionSocket.recv(1024).decode())
    print('Provided hash is: ' + passHash)

# Handles the worker connections, using if statements to determine wordload distribution based on number of connected workers
def workerHandler(connectionSocket, workers, requesters):
    try:
        global passHash
        while True:
            sendHash = ""
            if len(requesters) == 1:
                if passHash != "":
                    sendHash = passHash
                    connectionSocket.send(sendHash.encode())
                if len(workers) == 1:
                    time.sleep(0.1)
                    parameters = "123456"
                    workers[0].send(parameters.encode())
                    if sendHash != "":
                        break
                elif len(workers) == 2:
                    time.sleep(0.1)
                    parameters = "16"
                    workers[0].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "2345"
                    workers[1].send(parameters.encode())
                    if sendHash != "":
                        break
                elif len(workers) == 3:
                    parameters = "6"
                    workers[0].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "15"
                    workers[1].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "234"
                    workers[2].send(parameters.encode())
                    if sendHash != "":
                        break
                elif len(workers) == 4:
                    parameters = "6"
                    workers[0].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "5"
                    workers[1].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "14"
                    workers[2].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "23"
                    workers[3].send(parameters.encode())
                    if sendHash != "":
                        break
                elif len(workers) == 5:
                    parameters = "6"
                    workers[0].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "5"
                    workers[1].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "4"
                    workers[2].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "3"
                    workers[3].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "12"
                    workers[4].send(parameters.encode())
                    if sendHash != "":
                        break
                elif len(workers) == 6:
                    parameters = "6"
                    workers[0].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "5"
                    workers[1].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "4"
                    workers[2].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "3"
                    workers[3].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "2"
                    workers[4].send(parameters.encode())
                    time.sleep(0.1)
                    parameters = "1"
                    workers[5].send(parameters.encode())
                    if sendHash != "":
                        break
                    
        # Loop to constantly check for a response from the workers in case they found the password
        while True:
            response = connectionSocket.recv(1024).decode()

            # Prints messages in server indicating a found password and sends those messages to the requester with the password
            if len(response) != 0:
                response = ('Password found! ' + response)
                print(response)
                print('Succesful crack, server will restart in ten seconds.')
                requesters[0].send(response.encode())
                time.sleep(10)

                # Closes all currently open worker connections
                for connection in workers:
                    connection.close()

                os.execl(sys.executable, sys.executable, *sys.argv)
    except ConnectionResetError:
        print(addr, 'has discconected.')

# Main method for identifying the connected clients and sending them to handlers / creating threads
while True:
    connectionSocket, addr = serverSocket.accept()

    print('Connection recieved from: ', addr)
    queryResponse = connectionSocket.recv(1024).decode()

    # Handles for the requester client
    if queryResponse == "1":

        # Makes sure there is not already a requester, and sends to the thread / handler if not
        if len(requesters) == 0:
            print(addr, " Is a requester.")
            requester = 1
            reqThread = threading.Thread(
                target=requestHandler, args=("no",), daemon=True)
            reqThread.start()
            requesters.append(connectionSocket)

        # If there is already a requester, prints out a denial message, sends to the new requester, and closes the connection
        else:
            requestOverflow = "Currently handling a differnet request, could not connect this request."
            print(requestOverflow)
            connectionSocket.send(requestOverflow.encode())
            connectionSocket.close()

    # Handles for the worker clients
    elif queryResponse == "2":
        
        # If max number is passed, restarts server
        if len(workers) == 6:
            maxMessage = "Worker overload, too many attempted connect, server restarting."
            connectionSocket.send(maxMessage.encode())
            print(maxMessage)
            connectionSocket.close()

        # If not, worker is added to list and a thread for them is made
        else:
            print(addr, " Is a worker.")
            workers.append(connectionSocket)
            workThread = threading.Thread(target=workerHandler, args=(
                connectionSocket, workers, requesters,), daemon=True)
            workerHandlers.append(connectionSocket)
            workThread.start()

    # If server does not recognized identifier, connection is closed
    else:
        invalidMessage = ("Server did not recognize response, connection will close shortly.")
        connectionSocket.send(invalidMessage.encode())
        time.sleep(5)
        connectionSocket.close()
