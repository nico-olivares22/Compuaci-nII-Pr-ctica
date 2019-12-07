import sys
import time
import os
from multiprocessing import Process, Pipe


def lector(conn):
    while True:
        print(f"\nLeyendo', '(PID:{os.getpid()} )': {conn.recv()}")



def escritor(conn):
    print("Primer proceso hijo PID:", os.getpid())
    sys.stdin = open(0)
    while True:
        print('Ingrese una linea: ')
        c = sys.stdin.readline()
        conn.send(c)
        time.sleep(.3)



if __name__ == "__main__":
    escritor_conn, lector_conn = Pipe()
    print("Soy el proceso padre...  Mi PID es:", os.getpid())
    print("----------------------------------------")

    time.sleep(1)
    p1 = Process(target=escritor, args=(escritor_conn,))
    p2 = Process(target=lector, args=(lector_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
