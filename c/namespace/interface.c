#include "interface.h"
#include <stdio.h>

long len(const char *str){
	if(str == 0) return -1; //null pointer
	long c = 0;
	while(str[c++] != '\0'){}
	return c;
}

void foo(){
	int i;
	char s[] = "hello world\n";
	for(i=0;i<len(s);i++) putchar( s[i] );
}

int bar(int d){
	putchar( (char)*(((unsigned char *)&d)+0) );
	putchar( (char)*(((unsigned char *)&d)+1) );
	putchar( (char)*(((unsigned char *)&d)+2) );
	putchar( (char)*(((unsigned char *)&d)+3) ); //an int is 4 bytes
	return d+1;
}

const struct _library library = {
    .foo = foo,
    .bar = bar,
    .tmp = 0x33323130
};
