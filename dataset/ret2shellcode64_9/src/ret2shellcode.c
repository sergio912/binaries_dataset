//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	
	char buffer[9000];
	printf("The buffer is at: %p\n",buffer);
	gets(buffer);
	return 0;
}
