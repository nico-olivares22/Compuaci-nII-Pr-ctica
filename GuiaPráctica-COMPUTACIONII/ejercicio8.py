
"""
Realice un programa que genere dos procesos. El proceso hijo1 enviará la señal
SIGUSR1 al proceso padre y mostrará la cadena "ping" cada 5 segundos. El proceso
padre, al recibir la señal SIGUSR1 enviará esta misma señal al proceso hijo2. El
proceso hijo2, al recibir dicha señal mostrará la cadena "pong" por pantalla.

Soy proceso hijo1 con PID=1545: "ping"
Soy proceso hijo2 con PID=1547: "pong"
[... 5 segundos mas tarde ...]
Soy proceso hijo1 con PID=1545: "ping"
Soy proceso hijo2 con PID=1547: "pong"
[... y así sucesivamente ...]

"""
import os
import time
import signal
import multiprocessing
from multiprocessing import Process


#Manejo de señales
def handler(signum,frame):
    return


#Registro de señales
signal.signal(signal.SIGUSR1,handler)


#Subproceso - Hijo 1
def child1(pid_p):
    while True:
        print('-----------------------------------------')
        print('Soy proceso Hijo 1 con PID=%s: "ping" ' %(os.getpid()))
        os.kill(pid_p,signal.SIGUSR1)
        time.sleep(5)


#Subproceso - Hijo 2
def child2():
    while True:
        print('Soy proceso Hijo 2 con PID=%s: "pong" ' %(os.getpid()))
        print('-----------------------------------------')
        signal.pause()


#Proceso - Padre
if __name__ == '__main__':
    pid_p=os.getpid()
    p1=Process(target=child1, args=(pid_p,))
    p2=Process(target=child2)
    p1.start()
    p2.start()
#Bucle de la señal
    while True:
        os.kill(p2.pid, signal.SIGUSR1)
        signal.pause()
