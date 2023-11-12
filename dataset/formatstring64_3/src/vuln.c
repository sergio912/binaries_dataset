//gcc -Wl,-z,norelro vuln.c -o vuln
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
	char str[1024];
	char exit_flag = 'n';
	while (exit_flag != 'y') {
		puts("Just type something:");
		fgets(str,1023,stdin);
		printf(str);
		printf("\nExit (y/n): ");
		scanf("%c",&exit_flag);
		getchar();
	}
	return 0;
}
