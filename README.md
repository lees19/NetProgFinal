# NetProgFinal
Network Programming Final

Description:

This project will implement a password cracker using a client-server architecture programmed on Python. The program will include a server, request clients and worker clients.

Getting Started:

Installation: 
1) To install the project, download all files from the project github. 
2) Make sure that the folders in the directory where you place the file have no spaces in their names, the server reset will not work if there are spaces in the directory.
3) Ensure that you have Python 3 installed to run the file

Running:
NOTE: Follow the steps in this order, as clients are meant to be run in a specific order
1) Open the server by double clicking the file titled server.
2) Open however many worker clients you wish to run (maximum of six) by double clicking the workerClient file
3) Open the request client by double clicking on the requestClient file
4) Type in the desired password into the request client and wait for the workers to crack the password
5) Upon completion, the server, requester, and succesful worker will automatically close
6) Manually close the remaining worker windows as they will continue to guess until they have completed their loops

Features:
1. A request client that connects to the server and sends a hash.
2. Server that divides brute force work using string parameters according to number of worker clients.
3. Server sending each worker parameters to generate strings within.
4. Workers that generate hash for strings within parameters until matching hash found or parameters. 
5. Workers send correct hash or finish code to server.
6. Upon receiving correct string, server sends end signal to any workers still working and sends string to request client.

Demo Video:
https://youtu.be/8yMsHXsHlgc

References:

Torres, Andres. “Hashing Strings with Python.” Python Central, 13 Aug. 2013,www.pythoncentral.io/hashing-strings-with-  python/.

Python Software Foundation. “1. Command Line and Environment¶.” 1. Command Line and Environment -	 Python 3.8.0   Documentation, 2019,										 docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED.

Rohatgi, Shwetanshu. “Global and Local Variables in Python.” GeeksforGeeks, 6 Sept. 2018,			 www.geeksforgeeks.org/global-local-variables-python/.

Vairamani, Sakthipryan “How to Check a String for a Special Character?” Stack Overflow, 1 Jan. 1964,			 stackoverflow.com/questions/19970532/how-to-check-a-string-for-a-special-character.

Team Members:

Nick Quadros, Programmer

Luke Wooten, Programmer
