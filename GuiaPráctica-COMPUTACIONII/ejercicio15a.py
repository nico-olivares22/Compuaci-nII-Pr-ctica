"""
Ejercicio 16 – Multiprocessing / Pipe / FIFO
Replicar el comportamiento del ejercicio 12 utilizando el módulo Multiprocessing para
la creación del proceso hijo del programa consumidor.
"""

import os,sys,time
fifo= '/tmp/pipe_test'
def productor():
    fifo_fd = open(fifo,"w")
    print("Proceso padre")
    fifo_fd.write(sys.argv[1]+"\n")
    time.sleep(1)
if not os.path.exists(fifo):
    os.mkfifo(fifo)

productor()