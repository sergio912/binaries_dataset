//gcc vuln.c -o vuln -no-pie -fno-stack-protector
#include <stdio.h>

int main() {
	char str[24];
	printf("Welcome to the most useless program.\nJust type something: ");
	scanf("%s",str);
	return 0;
}
