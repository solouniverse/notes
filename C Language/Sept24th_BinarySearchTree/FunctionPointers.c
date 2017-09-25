#include <stdio.h>

void printOnce(int i)
{
	printf("%d\n", i);
}

void printTwice(int i)
{
	printf("%d %d\n", i, i);
}

int main(void)
{
	int i=12;
	void (*funP)(int);
	printf("Enter num of  times:");
	scanf("%d",&i);
	if(i==2)
		funP = & printTwice;
	else
		funP = & printOnce;
		
	funP(11);	
}
