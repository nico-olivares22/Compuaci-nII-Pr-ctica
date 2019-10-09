import sys
import time
import os
import multiprocessing
from multiprocessing import Process, Pipe


def lector(conn):

    print("Segundo proceso hijo PID:", os.getpid())
    print("Imprimiendo los mensajes escritos en el pipe.")
    print(lector_conn.recv())
    print("----------------------------------------")


def escritor(conn):
    print("Primer proceso hijo PID:", os.getpid())
    #for line in sys.stdin:
        #print(line)
    line="Este mensaje fue predefinido hasta encontrar la solucion ..."
    print("El mensaje fue escrito!")
    print("----------------------------------------")
    conn.send(line)
    conn.close()


if __name__ == "__main__":
    escritor_conn, lector_conn = Pipe()
    print("Soy el proceso padre...  Mi PID es:", os.getpid())
    print("----------------------------------------")

    time.sleep(1)
    p1 = Process(target=escritor, args=(escritor_conn,))
    p1.start()
    time.sleep(4)
    p1.join()
    p2 = Process(target=lector, args=(lector_conn,))
    p2.start()
    time.sleep(3)
    p2.join()
