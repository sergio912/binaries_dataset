//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <stdio.h>

int main() {
	char x[24];
	printf("Buffer is at address: %p\n",x);
	gets(x);
	return 0;
}
