"""Ejercicio 13 – Multiprocessing
Escribir un programa que genere tres procesos hijos (fork) cuyos nombres serán
“Hijo1”, “Hijo2” e “Hijo3”.
El proceso padre debe mostrar por pantalla el mensaje “Lanzando hijo NN” en la
medida que ejecuta cada uno de los procesos.
Cada hijo que se lance mostrará por pantalla su pid, el pid de su padre, esperará un
segundo, y luego terminará.
El padre debe esperar a la terminación de sus hijos."""
import os
import time
from multiprocessing import Process


#función reducida en 1
def childProcess(x, pid):
    print("Process -", x, ", PID Hijo:", os.getpid(), ", PID Padre:", pid)


# Padre
if __name__ == '__main__':
    pid = os.getpid()
    for x in range(1, 4):
        p = Process(target=childProcess, args=(x, pid))
        p.start()
        p.join()
