//SriMatreNamaha
#include <stdio.h>
#define MAX 5
void intro_to_pointers()
{
	int * pi;
	int variable = 1234;
	pi = &variable;
	printf("Value of variable=%d\n",variable);
	printf("Address of variable = %u\n",&variable);
	printf("*(&variable) = %u\n", *(&variable));
	printf("Value of pi=%u\n", pi);
	printf("Value poited by pi=%u\n", *pi);	
}
void intro2()
{
	int variable[5]={1,22,333,4444,55555};
	int temp;
	printf("%d\n", variable);
	printf("%d\n", &variable[0]);
	printf("%d\n", variable+1);
	printf("%d\n", &variable[1]);
	printf("%d\n", *(variable+1));
	printf("%d\n", *(variable+2));
	printf("%d\n", *(variable+3));
	temp=*(variable+1);
	*(variable+1)=*(variable+2);
	*(variable+2)=temp;
	printf("%d\n", *(variable+1));
	printf("%d\n", *(variable+2));
	//printf("%d\n", *(variable+1));
}
void PointerInterchange()
{
	int *p1, *p2;
	int i=2020, j=1010;
	int * temp;
	printf("i=%d\n", i);
	printf("j=%d\n------\n", j);

	p1=&i;
	p2=&j;
	printf("p1=%u\n", p1);
	printf("p2=%u\n------\n", p2);
	
	printf("*p1=%u\n", *p1);
	printf("*p2=%u\n------\n", *p2);

	temp=p1;
	p1=p2;
	p2=temp;
	printf("i=%d\n", i);
	printf("j=%d\n------\n", j);

	printf("p1=%u\n", p1);
	printf("p2=%u\n------\n", p2);

	printf("*p1=%u\n", *p1);
	printf("*p2=%u\n------\n", *p2);
}

void StructPointers()
{
	int i;
	
	struct node {
		struct node * pi;
		int variable;
	} node1[MAX];
	
	node1[0].variable=123;
	node1[1].variable=23;
	node1[2].variable=3;
	node1[3].variable=4;
	node1[4].variable=5123;

	for (i=0;i<MAX;i++)
		printf("node[%d].variable=%d\n", i, node1[i].variable);
		
	node1[0].pi = &node1[1];
	node1[1].pi = &node1[2];
	node1[2].pi = &node1[3];
	node1[3].pi = &node1[4];
	node1[4].pi = &node1[0];

/*
	printf("\nnode1[1].variable=\t\t%d\n",node1[1].variable);
	printf("(struct node *)(&node1[1])->variable=\t%d\n", (struct node *)(&node1[1])->variable);
	printf("(node1[0].pi)->variable=\t%d\n",(node1[0].pi)->variable);
*/
	for (i=0;i<MAX;i++)
		printf("(node1[%d].pi)->variable=\t%d\n", i,(node1[i].pi)->variable);
}

void main()
{
	int i=234;
	int *pi;
	int **ppi;
	int ***pppi;
	
	printf("i=\t%d\n", i);	
	printf("*&i=\t%d\n", *&i);	
	
	pi=&i;
	
	printf("*pi=\t%d\n", *pi);	
	printf("*(*&pi)=\t%d\n", *(*&pi));
	
	ppi=&pi;	
	
	printf("**ppi=\t%d\n", **ppi);
	printf("**(*&ppi)=\t%d\n", **(*&ppi));
	
	pppi=&ppi;
	
	printf("***ppi=\t%d\n", ***pppi);

}










