//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <ctype.h>
#include <stdio.h>
#include <string.h>

char buffer[128];

int main() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	
	printf("1 - Print some string\n");
	printf("2 - Give me something to print\n");
	printf("> ");
	
	int op = 0;
	scanf("%d",&op);
	getchar();
	
	switch(op) {
		case 1:
			printf("Some string.\n");
		break;
		case 2:
			gets(buffer);
			printf("%s",buffer);
		break;
		default:
			printf("Invalid option.\n");
	}
	return 0;
}
