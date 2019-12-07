"""Ejercicio 26 – Sock Inet Stream / fork
Escribir un programa servidor que levante un socket INET STREAM en todas las
direcciones locales, y en un puerto específico que será pasado por parámetros de línea
de comandos.
El servidor debe escuchar en el puerto especificado, y debe permitir, mediante
subprocesos (fork) atender a varios clientes simultáneamente.
Ejecutar el servidor, por ejemplo, así:
./servidor 1234
Escribir un programa cliente que utilice sockets INET STREAM que reciba por
parámetros dirección ip del servidor y puerto de esta forma:
./cliente 127.0.0.1 1234
El cliente con esos datos debe conectarse al servidor al puerto especificado, y luego
debe leer desde la entrada estándar (STDIN_FILENO) y todo lo que el usuario escriba
debe ir enviandoselo al servidor. El servidor los recibirá e irá mostrándolos por pantalla
junto con el identificador del proceso hijo que atiende al cliente conectado, la
dirección del cliente, y su puerto cliente.
Cuando el usuario escriba "exit" el cliente debe terminar la conexión y cerrar. El
servidor debe cerrar la conexión con ese cliente. """
import socket, sys, os, time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error: #si algo de arriba anduvo mal muestra el error del socket
    print ('Fallo al crear el socket!')
    sys.exit()
print ('Socket Creado!')

host = str(sys.argv[1])
port = int(sys.argv[2])

s.connect((host, port))

print ('Socket conectado al host', host, 'en el puerto', port)

while True:
    msg = input('Ingrese msg: ').encode()
    if msg.decode() == 'exit': #con exit sale del while y termina con la ejecución del programa 
        break
    else:
        try :
            #Set the whole string
            s.sendto(msg,(host, port))
        except socket.error:
            #Send failed
            print ('Fallo al enviar el msg!')
            sys.exit()

s.close()
