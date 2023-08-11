~~# Python and C script for copie_scr.sh decrypt/encrypt.
This is Python script to encrypt/decrypt MMI3GP copie_scr.sh file to be
automatically run when insert to system on a SD card for MMI3G(P) and RNS850 units.
~~
It uses .so libary to run seedkey calculation on .C and to AND calculation
on python.
~~
C is compiled as shared libary:~~
~~```~~
~~gcc -shared -Wl,-soname,<nameoflibary> -o <outputfile>.so -fPIC <sourcecode>.c
~~```~~

# Python Only script for En/Decrypting copie_scr.sh
Rewisited the code and made it Python Only after becomming smarter after years.
- Python is run with command python3 <name>.py <inputfile.sh> <outputfile.sh>
