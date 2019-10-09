import os
import sys
import time
import multiprocessing
from multiprocessing import Process, Pipe

fifo ='/tmp/pipe_chat'


def ejecucionA():
    # Abrir fifo para que el programa AA quede escuchando.
    if not os.path.exists(fifo):
        os.mkfifo(fifo)
    fifo_fd = os.open(fifo, os.O_RDWR)
    print("Estableciendo conexion con el chat.....")
    while True:


        line = os.read(fifo_fd,40)
        print("BB escribió:", line)
        # A este punto se debería haber mostrado el mensaje que envio BB
        # Procedemos a que AA pueda escribir un nuevo mensaje.
        print("---------------------")
        print("Escriba el mensaje para transmitirselo a BB \n")
        mensaje = input()
        os.write(fifo_fd,str.encode(mensaje))
        print("Mensaje enviado!")



ejecucionA()
