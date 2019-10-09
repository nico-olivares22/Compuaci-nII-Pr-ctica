import os,sys,time,multiprocessing
from multiprocessing import Process, Pipe
fifo='/tmp/pipe_chat'
def ejecucionB():
    #Abrir el fifo para que BB pueda leer y escribir sobre el
    if not os.path.exists(fifo):
        os.mkfifo(fifo)
    fifo_fd = os.open(fifo,os.O_RDWR)
    print("Estableciendo conexion con el chat")
    while True:


        print("Escriba su mensaje -> Será enviado a AA")
        mensaje=input()
        os.write(fifo_fd,str.encode(mensaje))
        print("Su mensaje fue enviado con éxito!")
        print("---------------------------------")

        print("AA escribió:",str(os.read(fifo_fd,40),'utf-8'))

ejecucionB()
