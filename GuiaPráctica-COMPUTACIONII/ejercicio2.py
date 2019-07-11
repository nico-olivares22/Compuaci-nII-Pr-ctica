import getopt
import sys
import os
(opt,arg) = getopt.getopt(sys.argv[1:], 'i:o:')
for (op,ar) in opt:
    if(op=='-i'):
        if os.path.isfile (ar):
            fd=open(ar,'r')
        else:
            print("Error")
            break
    if(op=='-o'):
        fn=open(ar, 'w+')
renglon=fd.readline()
while renglon:
    fn.write(renglon)
    renglon=fd.readline()
fd.close()
fn.close()
