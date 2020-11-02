/*
 * All read, reads entire file into buffer
 * ToraNova, chia_jason96@live.com
 * 2020 Nov 02
 */

#include<stdio.h>
#include<stdlib.h>

/*
 * Sample program to read the entire
 * file into buffer
 */

unsigned int eofread(FILE *file, unsigned char **buffer){
	unsigned int out=0;
	char tmp;
	do{
		tmp = fgetc(file);
		out++;
	}while(tmp != EOF);
	fseek(file, 0, SEEK_SET); //seek to beginning
	*buffer = (unsigned char *)malloc(out);
	fread((*buffer), 1, out, file);
	return out;
}

int main(int argc, char *argv[]){
	if(argc > 1){
		FILE *input = fopen(argv[1], "r");
		unsigned char *buffer;
		unsigned int len;
		len = eofread(input, &buffer);
		printf("char count: %u\n",len);
		printf("%s",buffer);
		return 0;
	}else{
		return 1;
	}
}
