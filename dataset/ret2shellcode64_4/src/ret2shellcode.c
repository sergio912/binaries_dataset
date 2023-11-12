//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <stdio.h>

char x[200];

int main() {
	fgets(x,199,stdin);
	char small_buffer[24];
	gets(small_buffer);
	return 0;
}
