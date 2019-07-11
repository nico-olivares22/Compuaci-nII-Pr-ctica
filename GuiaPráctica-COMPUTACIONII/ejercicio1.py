import getopt
import sys
def sumar(numero,numero2):
    return numero+numero2
def restar(numero,numero2):
    return numero-numero2
def multiplicar(numero,numero2):
    return numero*numero2
def dividir(numero,numero2):
    return numero/numero2
(opt,arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')

for (op,ar) in opt:
    if(op=='-o'):
        if ar=='+':
            operador=ar
            operador=sumar
        elif ar=='-':
            operador=ar
            operador=restar
        elif ar=='*':
            operador=ar
            operador=multiplicar
        elif ar=='/':
            operador=ar
            operador=dividir
        else:
            print("OPCION NO VALIDA")
            sys.exit(0)
            break

    if(op=='-n'):
        numero=ar
        try:
            numero=int(numero)
        except:
            print("OPCIÓN NO VALIDA 1")
            sys.exit(0)
    if (op=='-m'):
        numero2=ar
        try:
            numero2=int(numero2)
        except:
            print ("OPCIÓN NO VALIDA 2")
            sys.exit(0)
print("El resultado es: %f" % operador(numero,numero2))
