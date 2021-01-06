/* encryption/decryption for copie_scr.sh script used on Audi/Volkswagen MMI (Becker/Harman) */
#include <stdio.h>

unsigned int prng_rand(unsigned int value) 
{
	
	unsigned int r1, r3, r0;
		
	r1 = (value >> 1) | (value << 31);
	r3 = ((r1 >> 16) & 0xFF) + r1;
	r1 = ((r3 >> 8) & 0xFF) << 16;
	r3 -= r1;
	
	return r3;
}