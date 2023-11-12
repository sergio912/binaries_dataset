//gcc ret2shellcode.c -o ret2shellcode -fno-stack-protector -no-pie -z execstack

#include <ctype.h>
#include <stdio.h>
#include <string.h>

void menu() {
	printf("1 - Get string length\n");
	printf("2 - Get all upper case\n");
	printf("3 - Exit\n");
}

void string_to_upper(char *v, char *upper_string) {
	int i = 0;
	for (i = 0; i < 200 || v[i] != 0; i++) {
		upper_string[i] = toupper(v[i]);
	}
}

int main() {
	
	char x[56];
	int op = 0;
	while (op != 3) {
		menu();
		printf("> ");
		scanf("%d",&op);
		getchar();
	
		switch (op) {
			case 1:
				printf("Please insert string: ");
				gets(x);
				int str_len = strlen(x);
				printf("String length is: %d\n\n",str_len);
				break;
			case 2:
				printf("%p",x);
				printf("Please insert string: ");
				gets(x);
				
				char v[200];
				string_to_upper(x,v);
				printf("String upper: %s\n\n",v);
				break;
			case 3:
				return 0;
			default:
				printf("Invalid option.\n");
		}
	}
	return 0;
}
