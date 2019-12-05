"""Ejercicio 25 – Sockets INET/STREAM
Replique el comportamiento del ejercicio anterior, esta vez utilizando protocolo de
transporte confiable (TCP).  """
import socket, getopt, time, sys, os

(opt,arg) = getopt.getopt(sys.argv[1:], 'a:p:')

print('opciones: ', opt)

a = ""
p = ""

for (op,ar) in opt:
    if (op == '-a'):
        a = ar
        print('Opcion -p exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -f exitosa!')
    else:
        print('Opcion incorrecta!')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = a
port = p

s.connect((host, port))

while True:
    msg = input('Ingrese msg: ').encode('ascii')
    try:
        s.sendto(msg,(host, port))
    except socket.error:
        print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()
sys.exit()
