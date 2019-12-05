"""Ejercicio 24 – Sockets INET/DGRAM
Escriba un programa cliente-servidor con sockets INET/DGRAM que tenga el siguiente
comportamiento.
1. El usuario ejecutará el programa servidor pasándole dos argumentos:
1. -p: El puerto en el que va a atender el servicio (por defecto debe atender en
todas las direcciones de red configuradas en el sistema operativo).
2. -f: Una ruta a un archivo de texto en blanco.
2. El servidor creará el socket con los datos especificados, y creará, si no existe, el
archivo de texto.
3. El cliente recibirá dos argumentos por línea de comandos: la dirección IP (-a) y
el puerto en el que atiende el servidor (-p).
4. El cliente comenzará a leer desde STDIN texto hasta que el usuario presione
Ctrl+d.
5. El cliente enviará todo el contenido por el socket al servidor.
6. El servidor leerá todo el contenido desde el socket hasta que encuentre un EOF.
7. El servidor almacenará todo el contenido en el archivo de texto creado. """
import socket, getopt, time, sys, os

(opt,arg) = getopt.getopt(sys.argv[1:], 'a:p:')

print('opciones: ', opt)

a = ""
p = ""

for (op,ar) in opt:
    if (op == '-a'):
        a = ar
        print('Opcion -a exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    else:
        print('Opcion incorrecta!')

#create dgram udp socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error:
    print('Error al crear el socket')
    sys.exit()

host = a
port = p

while True:
    msg = input('Ingrese msg: ').encode()
    try:
        s.sendto(msg, (host, port))
    except socket.error:
        print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()
