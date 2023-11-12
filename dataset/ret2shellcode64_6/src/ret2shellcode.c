//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main() {
	printf("Tell me something to print: ");
	char x[8];
	fgets(x,7,stdin);
	printf(x);
	
	printf("Good job!\n");
	
	char magic_word[88];
	printf("Now, tell me the magic string: ");
	fgets(magic_word,500,stdin);
	
	if (strncmp(magic_word,"welcome to pwn",14) != 0) {
		exit(0);
	}
	
	return 0;
}
