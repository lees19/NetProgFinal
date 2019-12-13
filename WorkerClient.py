from socket import *
import itertools
import string
import hashlib
import time

# Uses parameters to generate strings within them and check for correct hash against provided hash
def generator(numbers, hashed):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    iterator = 0
    done = 0

    # Loop for moving through list of parameters
    while iterator <= len(numbers):

        # itertools loop that uses the current parameter to generate strings
        for guess in itertools.product(chars, repeat=numbers[iterator]):
            iteration = (''.join(guess))
            iterationHash = hashlib.md5(iteration.encode()).hexdigest()

            # Checks for correct hash and sends it to server if it is before printing a success message and closing soon after
            if iterationHash == hashed:
                done = 1
                success = 'The password is: ' + iteration
                connectionSocket.send(success.encode())
                print(success)
                print(
                    "Thank you for contributing to the crack! The program will close in ten seconds.")
                time.sleep(10)
                exit()
                break

        # Breaks from the loop if work is done.
        if done == 1:
            break
        iterator += 1
    time.sleep(10)

# Converts string value of parameters into integers and puts in a list for the generator to use
def rangeFinder(parameters, hashed):
    numbers = list()

    # Loop to convert string parameters to integers
    for character in parameters:
        numbers.append(int(character))
    generator(numbers, hashed)


# Sets up sockets / variables needed for connection
connectionSocket = socket(AF_INET, SOCK_STREAM)
identifier = "2"
ip = 'localhost'
port = 21
connectionSocket.connect((ip, port))
connectionSocket.send(identifier.encode())

# Main method used for majority of printing out to terminal
print("Thank you for contributing to the password crack!")
print("We will be borrowing some processing power before automatically closing this window.")
parameters = connectionSocket.recv(1024).decode()
if parameters == 'Number of workers at capacity, connection dropped.':
    print(parameters)
while True:
    hashed = connectionSocket.recv(1024).decode()
    if hashed != "" and len(hashed) > 6:
        print('Parameters are: ' + parameters)
        print('Correct hash is: ' + hashed)
        print("Working. . .")
        rangeFinder(parameters, hashed)
