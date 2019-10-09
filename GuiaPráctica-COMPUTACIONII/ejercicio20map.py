import os, sys, getopt
from multiprocessing import Pool


def sacar_raiz(numero):
    return numero**(1/2)

if __name__=="__main__":
    numerosImpares = []
    numero = 0
    segundo_numero = 0

    (opt,arg) = getopt.getopt(sys.argv[1:], 'n:m:')

    for (op,ar) in opt:
        if (op == '-n'):
            numero = int(ar)
        elif (op == '-m'):
            segundo_numero = int(ar)

    pool = Pool()

    for x in range (numero, segundo_numero):
        if x % 2 != 0:
            numerosImpares.append(x)

    resultado = pool.map(sacar_raiz, numerosImpares)


    for x, y in zip (numerosImpares, resultado):
        print("La raiz cuadra de %d: %d" % (x,y))
