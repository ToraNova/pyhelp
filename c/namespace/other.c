#include "other.h"
#include <stdio.h>

long other_len(const char *str){
	if(str == 0) return -1; //null pointer
	long c = 0;
	while(str[c++] != '\0'){}
	return c;
}

void other_somefoo(){
	int i;
	char s[] = "hello from the new world\n";
	for(i=0;i<other_len(s);i++) putchar( s[i] );
}

int other_somebar(int d){
	putchar( (char)*(((unsigned char *)&d)+0) );
	putchar( (char)*(((unsigned char *)&d)+1) );
	putchar( (char)*(((unsigned char *)&d)+2) );
	putchar( (char)*(((unsigned char *)&d)+3) ); //an int is 4 bytes
	return d+1;
}

const struct _other another = {
    .foo = other_somefoo,
    .bar = other_somebar,
    .tmp = 0x33323130
};
