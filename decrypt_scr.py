import sys
import os
from os import path
from ctypes import *
import os.path

seed=0x1be3ac

decrypt = CDLL('./decrypt.so')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def seedkey():
    global seed
    seed=decrypt.prng_rand(seed)
    
def main(data):
    global seed
    for i in range (len(data)):
        print(chr(data[i] ^ (seed & 0xFF)), end ='')
        #print(hex(seed))
        newFile.write((data[i] ^ (seed & 0xFF)).to_bytes(2, byteorder='big'))
        seedkey()

if len(sys.argv)!=3:
    print("Usage: "+sys.argv[0]+" input _filename output_filename")
    sys.exit()
if path.exists(sys.argv[2]) == True:
    print("File already exists")
    sys.exit()

f=open(sys.argv[1],"rb")
data=f.read()
f.close()
newFile=open(sys.argv[2],'wb')
print("File size: %d" % len(data))
seedkey()
main(data)
newFile.close()

