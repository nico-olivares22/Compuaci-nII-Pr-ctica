import signal, os, time

def handler(signum, frame):
    print('\nEsta vez me saldré, INTENTALO NUEVAMENTE')
    signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGINT, handler)

time.sleep(100)
