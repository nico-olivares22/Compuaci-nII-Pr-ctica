from multiprocessing import Pool, TimeoutError,Queue
import time
import os



def f(x):
    print("Proceso %d,Pid: %d"%(x,os.getpid()))
    time.sleep(x)
    q.put(os.getpid())
def popQue():
    while q:
        print("%d\t" % q.get(),end="")
        if q.empty():
            break
            print("\n")



if __name__ == '__main__':
    q =Queue()
    pool = Pool()
    pool.map(f,range(10))
    time.sleep(2)
    os.system('clear')
    popQue()
