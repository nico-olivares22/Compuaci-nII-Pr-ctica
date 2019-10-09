import os,sys,time
fifo='/tmp/pipe_test'
def consumidor():
    fifo_fd=open(fifo,"r")
    line = fifo_fd.readline()[:-1]
    r,w=os.pipe()
    pid=os.fork()

    if pid:
        os.close(r)
        w=os.fdopen(w,"w")

        w.write(line)
        w.close()
        os.wait()
        sys.exit(0)
    else:
        time.sleep(1)
        os.close(w)
        r=os.fdopen(r)
        salida=r.readline()
        print("la salida del hijo es %s "%salida)
        r.close()
        sys.exit(0)
consumidor()
