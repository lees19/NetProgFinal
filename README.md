# NetProgFinal
Network Programming Final

Description:
This project will implement a password cracker using a client-server architecture programmed on Python. The program will include a server, request clients and worker clients.

Deliverables:
We wish to deliver a working program as well as a detailed presentation. We will also deliver a detailed report outlining the project and our process through it, as well as weekly email updates logging what we have accomplished. 

Features:
1. A request client that connects to the server and sends a hash.
2. Server that divides brute force work using string parameters according to number of worker clients.
3. Server sending each worker parameters to generate strings within.
4. Workers that generate hash for strings within parameters until matching hash found or parameters. 
5. Workers send correct hash or finish code to server.
6. Upon receiving correct string, server sends end signal to any workers still working and sends string to request client.

Team Members:

Nick Quadros, Programmer
Luke Wooten, Programmer
