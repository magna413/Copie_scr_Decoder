import sys
import os
from os import path

seed = 0x1be3ac

os.system('cls' if os.name=='nt' else 'clear')

def seedkey(seed):
    mask = 2 ** 32 - 1
    r1 = seed >> 1 | ((seed << 31) & mask)
    r3 = ((r1 >> 16) & 0xFF) + r1
    r1 = ((r3 >> 8 & 0xFF) << 16) & mask
    r3 -= r1
    return r3 & mask

def main(data):
    global seed
    seed = seedkey(seed)
    for i in range (len(data)):
        print(chr(data[i] ^ (seed & 0xFF)), end ='')
        newFile.write(bytes([data[i] ^ (seed & 0xFF)]))
        seed = seedkey(seed)
        

if len(sys.argv)!=3:
    print("Usage: "+sys.argv[0]+" input _filename output_filename")
    sys.exit()
if path.exists(sys.argv[2]) == True:
    print("File already exists")
    sys.exit()

if path.exists(sys.argv[1]) == True:
    f=open(sys.argv[1],"rb")
else:
    print("Input file missing")
    sys.exit()

data=f.read()
f.close()
newFile=open(sys.argv[2],'wb')
print("File size: %d" % len(data))
main(data)
newFile.close()

