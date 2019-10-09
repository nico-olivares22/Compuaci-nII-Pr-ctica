import os,sys,time
from multiprocessing import Process,Pipe
fifo='/tmp/pipe_test'
def padre():
    fifo_fd=open(fifo,"r")
    line=fifo_fd.readline()
    lector_conn, escritor_conn = Pipe()
    pid = Process(target=hijo,args=(lector_conn,))
    escritor_conn.send(line)
    escritor_conn.close()
    pid.start()
    time.sleep(4)
    sys.exit(0)

def hijo(lector_conn):
    time.sleep(1)
    print("El mensaje recibido es: ",lector_conn.recv())
    sys.exit(0)
    pid.join()
    pid.close()
padre()
hijo()