"""Ejercicio 29 – Sock Inet Str / threading
Escriba un servidor tcp que atienda un puerto pasado por argumento (-p en getopt), y
reciba los siguientes comandos: ABRIR, CERRAR, AGREGAR, y LEER, por parte de los
clientes.
Si el cliente envía un comando ABRIR, el servidor deberá solicitarle un nombre de
archivo.
Si el cliente envía un comando "AGREGAR" el servidor deberá solicitarle una cadena
de texto para agregar al final del archivo.
Si el cliente envía un comando "LEER" el servidor le deberá enviar al cliente el
contenido del archivo.
Si el cliente envía un comando "CERRAR" el servidor deberá cerrar el archivo y cerrar
la comunicación con el cliente.
El servidor deberá poder mantener conexiones en simultáneo con varios clientes
mediante un sistema multihilo.
Deberá también programar a los clientes para que le soliciten comandos al usuario
mediante un simple menú de opciones, e interactúe con el servidor para que pueda
realizar sus tareas."""
import socket
import sys
import os
import getopt
import time

(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

for (op, ar) in opt:
    if op == '-a':
        a = str(ar)
    elif op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear el socket!')
    sys.exit()

print('Socket Creado!')

host = a
port = p

client.connect((host, port))

print('Socket conectado al host', host, 'en el puerto', port)

while True:

    print("""\n
    \t\t\t *** Menu ***
    - ABRIR
    - AGREGAR
    - LEER
    - CERRAR
    """)

    opcion = input('Opcion: ').upper()

    client.sendto(opcion.encode(), (host, port))

    if (opcion == 'ABRIR'):
        directorio = 'tmp/'
        try:
            os.stat(directorio)
        except:
            os.mkdir(directorio)
        print(client.recv(1024).decode())
        data = input()
        archivo = 'tmp/' + data + '.txt'
        client.sendto(archivo.encode(), (host, port))

    elif (opcion == 'AGREGAR'):
        print(client.recv(1024).decode())
        while True:
            msg = input()
            client.sendto(msg.encode(), (host, port))
            if msg == 'quit':
                break

    elif (opcion == 'LEER'):
        contenido = client.recv(1024).decode()
        print('\nArchivo: ' + archivo + '\n')
        print(contenido)
        input('Apretar Enter...')

    elif (opcion == 'CERRAR'):
        break

    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')

client.close()
