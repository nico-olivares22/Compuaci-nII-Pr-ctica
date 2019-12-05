"""
Ejercicio 32 – ProcessPoolExecutor
Escriba una función que calcule la serie de Fibonacci para un argumento dado. El
programa hará uso de ProcessPoolExecutor para que calcule las series de Fibonacci de
una lista de números enteros comprendidos entre N y M, siendo estos dos valores
números enteros pasados por argumento mediante las opciones “-n” y “-m” al
programa.
Así, un ejemplo de ejecución sería el siguiente:
./fibo_pool.py -n 5 -m 18
De este ejercicio se deben escribir dos versiones, una que utilice el algoritmo recursivo
para calcular la serie de Fibonacci, y otra que utilice el algoritmo iterativo.
"""
from concurrent.futures import ProcessPoolExecutor
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
    pool=ProcessPoolExecutor(resta)
    print("Ingrese -n como parametro mas pequeño.")
    while(n<m):
        for i in range(n):
            future=pool.submit(iter_fibo,n)
        n+=1
        print(future.result())