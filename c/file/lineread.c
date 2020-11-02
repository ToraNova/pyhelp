/*
 * Line reader example
 * ToraNova, chia_jason96@live.com
 * 2020 Apr 12
 */

#include<stdio.h>
#include<stdlib.h>

/*
 * Sample program to read a file
 * line by line into an array
 */

//#define DEBUG

// line read function,
// This is only applicable for printable texts
// file  -- an opened file stream, can be stdin too
// lines -- a reference to a unsigned char double pointer (a triple pointer)
// each element in lines, lines[0], lines[1] is a unsigned char array that is a line
// lens -- a reference to a unsigned int pointer (a double pointer)
// each element in lens is the length of the corresponding unsigned char array
// returns the number of lines read
// cannot read a file more than 4294967295 lines
// return 0 when nothing can be read (empty file)
unsigned int lineread(FILE *file, unsigned char ***lines, unsigned int **lens){
	unsigned int out, lc;
	char tmp; long int b, e; //begin and end pos
	out = 0; lc = 0; //initialize line counters

	//first PASS to count how many lines
	do{
		tmp = fgetc(file);
		if(tmp == '\n') out++; //increment counter if tmp is a newline
	}while(tmp != EOF); //do while we are not at the end of file
	fseek(file, 0, SEEK_SET); //seek to beginning
	//allocate memory for main out, the number of lines
	*lines = (unsigned char **)malloc((out)*sizeof(unsigned char *));
	*lens = (unsigned int *)malloc((out)*sizeof(unsigned int));
	while (lc <= out){
		b = ftell(file); //obtain start position
		do{
			tmp = fgetc(file);
			if(tmp == '\n' || tmp == EOF){
				//obtain last position, exclude \n or EOF
				e = ftell(file) - b - 1;
				break;
			}
		}while(1);
		fseek(file, b, SEEK_SET); //seek to new beginning (newline)
		(*lens)[lc] = e;
		(*lines)[lc] = (unsigned char *)malloc(e); //allocate space
		fread((*lines)[lc], 1, e, file); //read the line into buffer (as char, 1)
		if(tmp == EOF) break; //break immediately if end of file
		//read back the excluded EOF since we seeked past it
		tmp = fgetc(file); //newline is discarded
		lc++; //increment line counter
	}
	return out;
}

//DRIVER TEST
int main(int argc, char *argv[]){
	if( argc > 1){
		FILE *input = fopen(argv[1], "r");
		unsigned char **lines;
		unsigned int c, *lens;
		c = lineread(input, &lines, &lens);
		printf("lines read: %u\n",c);
		for(unsigned int i=0;i<c;i++){
			printf("%u(%u):%s\n",i,lens[i],lines[i]);
		}
		return 0;
	}
	else{
		return 1;
	}
}
