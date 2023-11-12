//gcc ret2win.c -no-pie -fno-stack-protector -o ret2win

#include <stdio.h>
#include <stdlib.h>

void win() {
	system("/bin/sh");
}

int main() {
	char s[900];
	fgets(s,1300,stdin);
	return 0;
}
