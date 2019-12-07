"""
Ejercicio 30 – Lock (multiprocessing)
Escriba un programa que lance 15 procesos hijos. El programa recibirá, mediante el
uso del modificador “-f”, un nombre de archivo que deberá crear o, si ya existe, abrir y
limpiar. Además, recibirá por argumento un número mediante el modificador “-r”. Ese
número representará la cantidad de iteraciones (ver más adelante).
Una llamada típica al programa podría ser:
./programa -r 5 -f /tmp/test.txt
Cada proceso tendrá asociada una letra del alfabeto (A, B, C, etc.), y deberá escribir
“su” letra tantas veces como iteraciones se hayan especificado con “-r”, y con un
delay de 1 segundo. Es decir, con la llamada anterior, cada proceso deberá escribir
una letra (“A”, “B”, etc) 5 veces con intervalo de un segundo... de esa forma, el
programa completo no demorará más de 5 segundos (todos los procs corren en
paralelo).
Haga uso de lock para que las N letras (5 en el ejemplo) escritas por cada proceso se
mantengan juntas y no intercaladas con los demás.
El resultado en el archivo del ejemplo será algo así:
AAAAADDDDDEEEEEBBBBB ...
Y no algo así
AABADDEBABEFBFAGGHD...
"""
import time
import sys
import getopt
from multiprocessing import Process,Lock
import string
(opt,arg)=getopt.getopt(sys.argv[1:],'f:r:',["archivo","iteraciones"])


def f(lock,file_name,n,letra):
    lock.acquire()
    file = open(file_name, 'a')
    for i in range(n):
        file.write(letra)
    time.sleep(1)
    file.close()
    lock.release()


if __name__=="__main__":
    for (op, ar) in opt:
        if (op in ['-f', 'archivo']):
            nombre_archivo=ar
        if (op in ['-r', 'iteraciones']):
            cant_iteraciones = int(ar)
    lock=Lock()
    letras = string.ascii_uppercase
    try:
        aux=open(nombre_archivo,'r+')
        contenido=aux.read()
        if contenido!='':
            aux.seek(0)
            aux.truncate() #Borramos el contenido del archivo solo si este fue escrito anteriormente
        aux.close()
    except FileNotFoundError as e:
        file=open(nombre_archivo,'a') #abrimos archivo
        file.close()
    lista=[]
    for i in range(15):
        letra=letras[i]
        lista.append(Process(target=f,args=(lock,nombre_archivo,cant_iteraciones,letra)))
        lista[i].start()
    for i in lista:
        i.join()
