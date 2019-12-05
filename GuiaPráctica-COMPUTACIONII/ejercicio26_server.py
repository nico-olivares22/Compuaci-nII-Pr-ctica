#!/usr/bin/python3
import sys
import socket
import os

# create a socket object
try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear el socket!')
    sys.exit()

# get local machine name
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    address = addr[0]
    port = addr[1]
    print('Conexion establecida')
    child_pid = os.fork()
    if not child_pid:
        while True:
            msg = clientsocket.recv(1024)
            print('\nChild Process: %s - Address: %s - Port: %d' %
                  (os.getpid(), address, port))
            print("Recibido: %s" % (msg.decode()))
            if not msg:
                break
        clientsocket.close()
