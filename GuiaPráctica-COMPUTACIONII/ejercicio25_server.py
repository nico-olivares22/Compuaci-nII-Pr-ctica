#!/usr/bin/python3
import socket, sys, time, getopt, os

(opt,arg) = getopt.getopt(sys.argv[1:], 'p:f:')

print('opciones: ', opt)

p = ""
f = ""

for (op,ar) in opt:
    if (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    elif (op == '-f'):
        f = ('tmp/'+ar)
        print('Opcion -f exitosa!')
    else:
        print('Opcion incorrecta!')

#create a socket object
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = ""
port = p

serv.bind((host, port))
serv.listen(5)

fd = open(f, "w+")

while True:
    conn, addr = serv.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        print('Address: %s - Port: %d' %(addr[0], addr[1]))
        print('Recibido: '+data.decode('ascii'))
        fd.write('\n'+data.decode('ascii'))
        time.sleep(1)

    conn.close()
    print('client disconnect')
