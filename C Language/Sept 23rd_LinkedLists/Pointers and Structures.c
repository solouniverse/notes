//SriMatreNamaha
#include <stdio.h>
#define MAX 5
struct node {
	struct node * pi;
	struct node * pSprev;
	int variable;
};

struct DoubleNode {
	struct node * pLinkL;
	struct node * pLinkR;
	int variable;
};


typedef struct node Node;
void intro_to_pointers()
{
	int * pi;
	int variable = 1234;
	pi = &variable;
	printf("Value of variable=%d\n", variable);
	printf("Address of variable = %u\n", &variable);
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
	};

	//struct node node1[MAX];
	typedef struct node Node;
	Node node1[MAX];
	
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

void multiLevelPointers()
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

void PrintList(Node * head)
{
	printf("From %s ____\n",__func__);
	do{
		printf("*pNode(%u)=\t%d\n", head, head->variable);
		head = head->pi;
	}while(head != NULL);
}

void PrintList2(Node * head)
{
	if((head != NULL)){
		printf("*pNode(%u)=\t%d\n", head, head->variable);
		PrintList2(head->pi);
	}
}

void PrintListReverse(Node * head)
{
	if((head != NULL)){
		PrintListReverse(head->pi);
		printf("*pNode(%u)=\t%d\n", head, head->variable);
	}
}

Node * ListReverse(Node * current, Node * pPrev)
{
	Node * pTemp;
	
	if((current->pi != NULL)){
		pTemp=ListReverse(current->pi, current);
		current->pi = pPrev;
		return pTemp;
	}else{
		current->pi = pPrev;
		return current;
	}
}

int FindLoops(Node * head)
{
	Node * pHead;
	Node * pHead2;
	
	int CircularFound=0;
	
	pHead=head;
	pHead2 = pHead->pi;
	
	while ((pHead != NULL) && (pHead2 != NULL)) {
		if ( pHead == pHead2){
				printf("Found a circular link @%u:%u\n", pHead,pHead2);
				return(1);
		}
		pHead = pHead->pi;
		if((pHead2->pi != NULL))
			pHead2 = (Node *)(pHead2->pi)->pi;
		else
			break;
	}
	return(0);
}

int main(void)
{
	int i;
	int counter=0, CircularFound=0;
	

	Node node1[MAX];
	Node * pHead;
	Node * pHead2;
	Node * pAddress[MAX];
	
	node1[0].variable=123;
	node1[1].variable=23;
	node1[2].variable=3;
	node1[3].variable=4;
	node1[4].variable=5123;

	node1[0].pi = &node1[1];
	node1[1].pi = &node1[2];
	node1[2].pi = &node1[3];
	node1[3].pi = &node1[4];
	node1[4].pi = &node1[1];
	
	pHead=&node1[0];
	
	for (i=0;i<MAX;i++)
		printf("node[%d].variable=%d \t&node[%d](%u)\tnode[%d].pi(%u)\n", i, node1[i].variable,i,&node1[i],i,node1[i].pi);
/*
	printf("\n------------------------------------------------\n");
	for (i=0;i<MAX;i++)
		printf("(node1[%d].pi)->variable=\t%d\n", i,(node1[i].pi)->variable);
		
	printf("\n------------------------------------------------\n");
	for (i=0;i<MAX;i++)
		printf("(*(node1[%d].pi)->pi)->variable=\t%d\n", i,((Node *)(node1[i].pi)->pi)->variable);
*/
	printf("\n------------------------------------------------\n");
	
/*
 * 	PrintList(pHead);
	printf("\n------------------------------------------------\n");
	printf("From PrintList2 ____\n");
	PrintList2(pHead);
	
	printf("\n------------------------------------------------\n");
	printf("From PrintListReverse ____\n");
	PrintListReverse(pHead);

	pHead = ListReverse(pHead, NULL);

	printf("\n------------------------------------------------\n");
	printf("After reversing, From PrintList2  ____\n");
	PrintList2(pHead);
*/

/*
// To find a circular Linked List
	while (pHead->pi != NULL ){
		if ( pHead->pi == &node1[0]){
			printf("Found a circular link @%d", pHead->pi);
			break;
		}
		pHead = pHead->pi;
	}
*/	

/*
// To find loops in singly linked list Using an Array.
// It uses an extra Data structures but finds out exact point of intersection!!!
	
	pHead=&node1[0];
	while ( pHead->pi != NULL ){
		for (i=0;i<counter;i++){
			if ( pHead->pi == pAddress[i]){
				printf("Found a circular link @%d", pHead);
				CircularFound=1;
				break;
			}
		}
		if(CircularFound==1)
			break;
		pAddress[counter++]=pHead;
		pHead = pHead->pi;
	}
	if(CircularFound != 1)
		printf("Its not a circular Linked List\n");
*/

// To find loops 
// Method 2: Without using extra Data structures.

/*	if(FindLoops(pHead))
		printf("Its a Circular List\n");
	else
		printf("Its a Straight List\n");
*/

/*
	do{
		printf("*pNode(%u)=\t%d\n", pNode, pNode->variable);
		pNode = pNode->pi;
	}while(pNode != &node1[0]);
*/
}



