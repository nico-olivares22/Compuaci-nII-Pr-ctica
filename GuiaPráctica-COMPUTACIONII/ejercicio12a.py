"""Crear un sistema Productor-Consumidor (Escritor-Lector) donde un proceso productor
almacene un mensaje de saludo en una tubería FIFO. Ese mensaje será enviado
mediante línea de comandos como argumento del programa. Ejemplo
./saludofifo HOLA
Otro programa (consumidor) deberá leer el mensaje desde la tubería FIFO, generar un
proceso hijo (fork) y enviarle por PIPE el mensaje. El proceso hijo mostrará por pantalla
el mensaje recibido."""
import os,sys,time
fifo= '/tmp/pipe_test'
def productor():
    fifo_fd = open(fifo,"w")
    print("Proceso padre")
    fifo_fd.write(sys.argv[1]+"\n")
    time.sleep(1)
if not os.path.exists(fifo):
    os.mkfifo(fifo)

productor()
