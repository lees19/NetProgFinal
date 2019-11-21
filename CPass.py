# Import socket module 
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys
import itertools
import string

# Set up chat client
HOST = input('Enter server host: ')
if not HOST:
    HOST = "localhost"

PORT = input('Enter server port: ')
if not PORT:
    PORT = 1234
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
NAME = ''

# Create a TCP client socket
client_socket = socket(AF_INET, SOCK_STREAM)
# Connect to the chat server
client_socket.connect(ADDR)

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            if msg == "{quit}":
                # Close the client socket after {quit} received by chat server
                client_socket.close()
        except OSError:
            # Possibly client has left the chat.
            break

def guess_password(range, real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            elif guess == range: 
                return 'password is not in this range'
            print(guess, attempts)


def main(): 
    type = input("1 for requester, 2 for worker")
    client_socket.send(type.encode("utf8"))
    #recv range to search within, the real password
    
    range = client_socket.recv(1024).decode("utf8")
    real = client_socket.recv(1024).decode("utf8")

    guess_password(range, real)



if __name__ == "__main__":
    Thread(target = main()).start()
    Thread(target = receive()).start()

'''
def Main(): 
	type = input("1 for requester, 2 for worker")
    client_socket.send()
    #range to search within, and the real password
client_socket.recv()
'''