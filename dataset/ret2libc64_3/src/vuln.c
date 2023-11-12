//gcc vuln.c -o vuln -no-pie -fno-stack-protector
#include <stdio.h>
#include <stdlib.h>

int main() {
	long static_canary = 0xaabbccddeeff1100;
	char str[24];
	puts("Welcome to the most useless program.\nJust type something:");
	gets(str);
	//Check if canary was changed
	if (static_canary != 0xaabbccddeeff1100) {
		printf("** Stack smashing detected, stopping execution! **");
		abort();
	}
	return 0;
}
