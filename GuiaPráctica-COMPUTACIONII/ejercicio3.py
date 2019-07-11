import os,time

def hijo():
    for x in range (5):
        print('Soy el Hijo')
        time.sleep(1)
    os._exit(0)
def padre():
    wpid=os.fork()
    if wpid==0:
        hijo()

    for x in range (2):
        print ('Soy el Padre')
        time.sleep(1)
    os.wait()
    print("El proceso hijo termino")

padre()
