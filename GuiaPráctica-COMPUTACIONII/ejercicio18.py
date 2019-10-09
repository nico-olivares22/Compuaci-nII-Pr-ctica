from multiprocessing import Process, Queue
import os,time
count=0
def f(q):
    q.put(["PID:", os.getpid()])


if __name__ == '__main__':
    lista =list()
    q = Queue()

    for x in range (1,11):
        lista.append( Process(name="Proceso",target=f, args=(q,)))
    for Proceso in lista:
        Proceso.start()
        count=count+1
        time.sleep(count)
        print(f"Proceso {count},PID: {Proceso.pid}")
    while q:
        Proceso.join()
        print(f"Contenido cola de mensajes: {q.get()}")
        if q.empty():
              print("Cola vacia... saliendo")
              break