//gcc vuln.c -o vuln -no-pie
#include <stdio.h>
#include <stdlib.h>

int main() {
	printf("Welcome to the most useless program.\n");
	char exit_flag = 'n';
	char str[24];
	while (exit_flag != 'y') {
		puts("Just type something:");
		gets(str);
		printf(str);
		printf("\nExit (y/n): ");
		scanf("%c",&exit_flag);
		getchar();
	}
	return 0;
}
