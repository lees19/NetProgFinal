from socket import *
import itertools
import string
import hashlib

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
print(hashed)
print('Parameters are: ' + parameters)
print('Correct hash is: ' + hashed)
print("Working. . .")
rangeFinder(parameters, hashed)

# Converts string value of parameters into integers and puts in a list for the generator to use
def rangeFinder(parameters, hashed):
    numbers = list()

    for character in parameters:
        numbers.append(int(character))
    generator(numbers, hashed)
        
# Uses parameters to generate strings within them and check for correct hash against provided hash
def generator(numbers, hashed):
    chars = string.ascii_lowercase + string.digits
    iterator = 0
    done = 0
    while iterator <= len(numbers):
        for guess in itertools.product(chars, repeat = numbers[iterator]):
            iteration = (''.join(guess))
            iterationHash = hashlib.md5(iteration.encode()).hexdigest()
            if iterationHash == hashed:
                done = 1
                success = 'The password is: ' + iteration
                connectionSocket.send(success.encode())
                print(success)
                print("Thank you for contributing to the password crack! The program will close momentarily.")
                break
        if done == 1:
            break
        iterator += 1
    
    for values in numbers:
        for guess in itertools.product(chars, repeat = numbers[values]):

            if guess == hashed:
                success = 'password is {}.'.format(guess)
                connectionSocket.send(success.encode())
                print (success)
                print("Thank you for contributing to the password crack! The program will close momentarily")
            elif guess == range: 
                failure = 'Failure to find password.'
                connectionSocket.send(failure.encode())
                print (failure)
                print("Thank you for contributing to the password crack! The program will close momentarily.")