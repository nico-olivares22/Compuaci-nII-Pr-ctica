import os
import multiprocessing
from multiprocessing import Process


def child1(x):
    print("Soy el proceso", os.getpid(), "mi padre es", x)


def child2(x):
    print("Soy el proceso", os.getpid(), "mi padre es", x)


def child3(x):
    print("Soy el proceso", os.getpid(), "mi padre es", x)


if __name__ == '__main__':
    print("Padre:", os.getpid())
    x=os.getpid()
    p1=Process(target=child1,args=(x,))
    p2=Process(target=child2,args=(x,))
    p3=Process(target=child3,args=(x,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
