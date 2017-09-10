#include <stdio.h>
int main(){
	char *name = "Sri RAM"; //Array[]
	char ch='c';
	int i=123;
	float f=123.5;
	double d=4334.4;
	printf("Contents of name= %u\n", sizeof(name));
	printf("Contents of ch= %u\n", sizeof(ch));
	printf("Contents of i= %u\n", sizeof(i));
	printf("Contents of f= %u\n", sizeof(f));
	printf("Contents of d= %u\n", sizeof(d));
	printf("Contents of name= %u\n", name);
	printf("Contents of name= %c\n", name);
	printf("Contents of name= %c\n", name[0]);
	printf("Contents of name= %s\n", name);
}

