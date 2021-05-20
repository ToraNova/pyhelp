/*
 * Example of opening and reading special file descriptors
 */

#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[], char *envp[]){

	unsigned char buff[6];

	int rc, i;
	//read from stdin (fd 0)
	rc = read(0, buff, 6); //read only 6 characters

	printf("read %d from stdin:", rc);
	for(i=0;i<6;i++){
		//printf("0x%02X ",buff[i]);
		printf("%d ",buff[i]);
	}
	printf("\n");
}
