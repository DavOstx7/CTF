#include <stdio.h>
#include <stdlib.h>



int main(){
	char* msg = (char*)malloc(8);
	read(0, msg, 8);
	printf("%s\n", msg);
	printf("msg[0] = %x, msg[1] = %x\n", msg[0], msg[1]);
	return 1;
}
