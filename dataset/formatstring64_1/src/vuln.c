//gcc vuln.c -o vuln -no-pie
#include <stdio.h>
#include <stdlib.h>

void win() {
	system("/bin/sh");
}

int main() {
	char str[32];
	scanf("%s",str);
	printf(str);
	return 0;
}
