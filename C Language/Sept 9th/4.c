#include <stdio.h>
int main(){
	char name[11]="Sri RAM"; //Array[]

	printf("Contents of name= %u\n", sizeof(name));
	printf("Contents of name= %u\n", name);
	printf("Contents of name= %c\n", name);
	printf("Contents of name= %s\n", name);
	printf("Address of name[0]= %u\n", &name[0]);
	printf("Address of name[1]= %u\n", &name[1]);
	printf("Address of name[2]= %u\n", &name[2]);
	printf("Contents of name[0]= '%c'\n", name[0]);
	printf("Contents of name[1]= '%c'\n", name[1]);
	printf("Contents of name[2]= '%c'\n", name[2]);
	printf("Contents of name[3]= '%c'\n", name[3]);
}

