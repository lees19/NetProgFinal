from socket import *
import threading
import itertools
import string

# Sets up sockets / variables needed for connection
connectionSocket = socket(AF_INET, SOCK_STREAM)
identifier = "2"
ip = 'localhost'
port = 21
connectionSocket.connect((ip, port))
connectionSocket.send(identifier.encode())

# Main method
hashed = connectionSocket.recv(1024).decode()
parameters = connectionSocket.recv(1024).decode()
generator(parameters, hashed)

def generator(parameters, hashed):
    chars = string.ascii_lowercase + string.digits

    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat = password_length):
            guess = ''.join(guess)

            if guess == hashed:
                success = 'password is {}.'.format(guess)
                connectionSocket.send(success.encode())
                print("Thank you for contributing to the password crack! The program will close momentarily")
            elif guess == range: 
                failure = 'Password is not in this range'
                connectionSocket.send(failure.encode())
                print("Thank you for contributing to the password crack! The program will close momentarily.")