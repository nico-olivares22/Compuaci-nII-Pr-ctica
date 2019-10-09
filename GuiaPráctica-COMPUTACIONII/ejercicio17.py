"""
Ejercicio 17 – Fork / MQ
Escriba un programa que cree diez procesos hijos (fork).
Cada proceso al iniciar debe escribir por pantalla "Proceso xx, PID: xxxx"
A su vez, cada proceso debe esperar i segundos, donde i es el número de proceso hijo,
y luego escribir en un formato "xxxxx\t" el pid en una cola de mensajes.
El padre debe esperar a que todos los hijos terminen, y luego leer el contenido de la
cola de mensajes y mostrarlo por pantalla.
"""
from multiprocessing import Process, Queue
import os,time

count=0

if __name__ == '__main__':
    q = Queue()

    for x in range (1,11):
        newpid = os.fork()
        if newpid == 0:
            os._exit(0)
        else:
            q.put(["PID:", newpid])
            count=count+1
            time.sleep(count)
            print(f"Proceso {count},PID: {newpid}")


    while q:
        count = count + 1
        print(f"Contenido cola de mensajes: {q.get()}")
        if q.empty():
              print("Cola vacia... saliendo")
              break

