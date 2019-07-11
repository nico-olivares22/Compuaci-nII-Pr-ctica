import os,sys,time,signal

def handler(signum,frame):
    return

signal.signal(signal.SIGUSR1,handler)
signal.signal(signal.SIGUSR2,handler)

def f2():
    r, w = os.pipe()
    print("Iniciando padre -A-")

    pB = os.fork()

    if pB==0:
        signal.pause()
        print("Mostrando los mensajes almacenados en la tubería:")
        print("Proceso hijo -B-")
        os.close(r)
        w = os.fdopen(w,'w')
        w.write("Mensaje1 PID:%s \n"%os.getpid())
        w.flush()
        time.sleep(1)
        pC = os.fork()
        os.kill(pC,signal.SIGUSR1)

        if pC==0:
            signal.pause()
            print("Proceso hijo -C-")
            w.write("Mensaje2 PID:%s \n"%os.getpid())
            w.close()

            os.kill(pB,signal.SIGUSR1)
            time.sleep(1)
            sys.exit(0)

    time.sleep(1)
    os.kill(pB,signal.SIGUSR1)

    signal.pause()
    r = os.fdopen(r,'r')

    for line in r:
        print("%s" % line)
    r.close()
    print("Cerrando extremo")
f2()
