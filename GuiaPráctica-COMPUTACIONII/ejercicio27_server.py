
import socket, os, multiprocessing, sys

def mp_server(sock):
    print("Launching process...")
    while True:
        msg = sock.recv(1024)
        print("Recibido: %s" % msg.decode())
        if not msg:
            break




# creamos un objeto de tipo socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    #se establece conexión
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    child = multiprocessing.Process(target=mp_server, args=(clientsocket,))
    child.start()
