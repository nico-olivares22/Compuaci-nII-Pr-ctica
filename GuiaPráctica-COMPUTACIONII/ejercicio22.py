"""Ejercicio 22 – Threading
Adaptar el ejercicio 13 para que haga uso de hilos con threading. Los hijos, además de
mostrar su PID y el PID del proceso padre, también deberán mostrar el identificador de
hilo de ejecución. """
from multiprocessing import Queue, Lock
import sys
import threading
import time
import os

def thread_function(x,l,q,pid):
    l.acquire()
    time.sleep(1)
    threadID = threading.get_ident()
    threadName = threading.current_thread().getName()
    q.put("Mi PID es: %d, ThreadName: %s, ThreadID: %d, Proceso: %d, Padre: %d"%(os.getpid(), threadName,threadID, x, pid))
    l.release()


def mostrarCola(q):
    while True:
        print (q.get())
        if q.empty():
            break



if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    pid = os.getpid()

    for x in range(3):
        th = threading.Thread(target=thread_function, args=(x,lock,q,pid))
        th.start()
        time.sleep(1)
        th.join()

    mostrarCola(q)
