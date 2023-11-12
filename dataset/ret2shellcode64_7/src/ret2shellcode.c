//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main() {
	setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

	int a = 0;
	int b = 0;
	
	char first_check[32];
	fgets(first_check,72,stdin);
	
	char buffer[24];
	if (a == 0x1337 && b == 0xcafe) {
		printf("%p",buffer);
		gets(buffer);
	}
	return 0;
}
