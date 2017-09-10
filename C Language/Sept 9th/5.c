#include <stdio.h>
int main(){
	char name[11]; //Array[]
	int age;
	printf("Enter name: ");
	scanf("%s %d", name, &age);
	printf("Contents of name= %s\n", name);
	printf("Contents of age= %d\n", age);
}
