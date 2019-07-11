import os
import sys
try:
    if (isinstance(int(sys.argv[1]),int) is True):
        procesohijo= os.fork()
        if procesohijo==0:
            print(f"Valor Decrementado: {int(sys.argv[1])-2}")
        else:
            print(f"Valor Incrementado: {int(sys.argv[1]) +4}")
except:
    print("Ingrese un numero entero")
    sys.exit(0)
