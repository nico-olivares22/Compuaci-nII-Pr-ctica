import os,time,signal

def handler(s,f):
    print("mensaje del padre al hijo")

def hijo():
    print("Iniciando Hijo")
    while True:
        print("Señal del Padre recibida")
        signal.pause()

signal.signal(signal.SIGUSR1,handler)
pid=os.fork()

if pid == 0:
    hijo()
else:
    print("Iniciando padre")
    while True:
        os.kill(pid,signal.SIGUSR1)
        time.sleep(5)
