//gcc vuln.c -o vuln -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int global_var = 0;

int main() {
	char str[512];
	fgets(str,511,stdin);
	printf(str);
	if (global_var == 0x1337) {
		system("/bin/sh");
	}
	return 0;
}
