import os,sys,time,signal

def handler(signum,frame):
    return

def hijo(w, r):
    signal.pause()
    os.close(r)
    w = os.fdopen(w,'w')
    w.write("Mensaje Hijo PID:%s \n"%os.getpid())
    w.close()

def nieto(w, r):
    signal.pause()
    os.close(r)
    w = os.fdopen(w, 'w')
    w.write("Mensaje Nieto PID:%s \n"%os.getpid())
    w.close()


pidAbuelo = os.getpid()

signal.signal(signal.SIGUSR1,handler)

def f2():
    r, w = os.pipe()
    print("Iniciando padre -A-")

    pB = os.fork()

    if pB==0:
        pC = os.fork()
        if pC==0:
            nieto(w, r)
            os.kill(pidAbuelo, signal.SIGUSR1)
            os._exit(0)
        else:
            hijo(w, r)
            time.sleep(0.001)
            os.kill(pC, signal.SIGUSR1)
            os.wait()
            os._exit(0)
    else:
        time.sleep(0.001)
        os.kill(pB,signal.SIGUSR1)
        signal.pause()
        os.close(w)
        r = os.fdopen(r, 'r')
        print("Padre (PID=%d) leyendo de la tuberia: \n" % os.getpid())
        linea = r.readline()
        while linea:
            print(linea)
            linea = r.readline()
        r.close
        os.wait()

f2()
