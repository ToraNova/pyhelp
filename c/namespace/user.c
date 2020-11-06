#include "interface.h"

int main(int argc, char *argv[]){
	library.foo();
	int d = library.bar(library.tmp);
	library.bar(d);
}
