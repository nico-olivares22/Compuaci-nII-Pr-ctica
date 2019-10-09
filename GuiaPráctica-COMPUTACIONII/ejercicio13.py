
import multiprocessing
from multiprocessing import Process
import os
import time


def child1():
     print("Hijo1", os.getpid())
     print("El pid de mi padre es:", os.getppid())
     print("---------------------------------------")

def child2():
        print("Hijo2", os.getpid())
        print("El pid de mi padre es:",os.getppid())
        print("---------------------------------------")
def child3():
     print("Hijo3",os.getpid())
     print("El pid de mi padre es:",os.getppid())
     print("---------------------------------------")


if __name__=="__main__":
    print("Soy el proceso padre. Mi pid es:",os.getpid())
    print("----------------------------------------")
    time.sleep(2)
    p1=Process(target=child1)
    p2=Process(target=child2)
    p3=Process(target=child3)
    print("Lanzando hijo 1")
    p1.start()
    time.sleep(2)
    p1.join()
    print("Lanzando hijo 2")
    p2.start()
    time.sleep(2)
    p2.join()
    print("Lanzando hijo 3")
    p3.start()
    time.sleep(2)
    p3.join()
    print("Finalizando proceso padre.")
