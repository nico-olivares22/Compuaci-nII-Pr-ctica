import os,time,signal

def handler(s,f):
    print("mensaje del hijo al padre")

def hijo1():
    print("Soy el Hijo1")
    while True:
        print("PING")
        time.sleep(5)
        signal.pause()
signal.signal(signal.SIGUSR1,handler)
pid=os.fork()
print(pid)

def hijo2():
    print("Soy el Hijo2")
    while True:
        print("PONG")
        signal.pause()

signal.signal(signal.SIGUSR1,handler)
pid=os.fork()
print(pid)
hijo2()
def padre():
    print("Iniciando padre")
    while True:
        os.kill(pid,signal.SIGUSR1)
        time.sleep(5)
signal.signal(signal.SIGUSR1,handler)
pid=os.fork()
