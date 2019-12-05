"""
Ejercicio 33 – ThreadPoolExecutor
Reescriba el programa anterior para ejecutarlo con hilos concurrentes mediante
ThreadPoolExecutor. Al igual que el ejercicio anterior, escribir una versión que utilice el
algoritmo recursivo y otra haciendo uso del algoritmo iterativo.
"""
from concurrent.futures import ThreadPoolExecutor
import sys
import getopt
(opt,arg)=getopt.getopt(sys.argv[1:],'n:m:',["numero1","numero2"])
def iter_fibo(n):
    a = 1
    b = 0
    for i in range(n):
        a, b = b, a + b
    return b

if __name__=="__main__":
    for (op,ar) in opt:
        if (op in ['-n', 'numero1']):
            n=int(ar)
        if (op in ['-m', 'numero2']):
            m=int(ar)

    resta=m-n
    pool=ThreadPoolExecutor(resta)
    print("Ingrese -n como parametro mas pequeño.")
    while(n<m):
        for i in range(n):
            future=pool.submit(iter_fibo,n)
        n+=1
        print(future.result())