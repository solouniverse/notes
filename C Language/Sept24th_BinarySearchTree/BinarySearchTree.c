#include <stdio.h>
#include <malloc.h>

#define MAX 9

struct TreeNode {
	struct TreeNode * pLinkL;
	struct TreeNode * pLinkR;
	int variable;
};
typedef struct TreeNode tNode;


tNode * AddNode(tNode * pHead, int value)
{
	tNode * pTemp;
	tNode * pTemp2;
	
	pTemp=malloc(sizeof(tNode));
	if(pTemp == NULL)
	{
		printf("Failed to allocate memory\n");
		exit(-1);
	}
	
	pTemp->pLinkL = NULL;
	pTemp->pLinkR = NULL;
	pTemp->variable = value;
	
//	printf("Please enter value for new node: "):
//	scanf("%d", &pTemp->variable);

	if(pHead == NULL)
	{
		//printf("Created head node just now!(%u)\n", pTemp);
		return pTemp;		
	}

	for(pTemp2=pHead; pTemp2 != NULL; )
	{
		//printf("inside for loop\n");
		if(pTemp2->variable > pTemp->variable)
		{	
			if (pTemp2->pLinkL == NULL)
			{
				pTemp2->pLinkL=pTemp;
				break;
			}
			pTemp2=pTemp2->pLinkL;
			//printf("Going to left\n");
		}
		else if(pTemp2->variable < pTemp->variable)
		{
			if (pTemp2->pLinkR == NULL)
			{
				pTemp2->pLinkR=pTemp;
				break;
			}
			pTemp2=pTemp2->pLinkR;
			//printf("Going to right\n");
		}
		if(pTemp2->variable == pTemp->variable)
		{
			//printf("Value already in the tree\n");
			free(pTemp);
			break;
		}			
	}
	return pHead;
}

void printTreeInOrder(tNode *pHead, int count)
{
	if (pHead  != NULL){
		printTreeInOrder(pHead->pLinkL,count+1);
		printf("%d ", pHead->variable);
		//printf("%d(%d) ", pHead->variable,count);
		printTreeInOrder(pHead->pLinkR, count+2);
	}
}

void printTreePreOrder(tNode *pHead)
{
	if (pHead  != NULL){
		printf("%d ", pHead->variable);
		printTreePreOrder(pHead->pLinkL);
		printTreePreOrder(pHead->pLinkR);
	}
}

void printTreePostOrder(tNode *pHead)
{
	if (pHead  != NULL){
		printTreePostOrder(pHead->pLinkL);
		printTreePostOrder(pHead->pLinkR);
		printf("%d ", pHead->variable);
	}
}

void main(void)
{
	tNode *pHead=NULL;
	int choice;
	int iArray[MAX] = {8,1,4,3,6,7,10,14,13};

	for (int i=0; i< MAX;i++){
		printf("%d ",iArray[i]);
		pHead = AddNode(pHead, iArray[i]);
	}
	printf("\nprintTreeInOrder:\n");
	printTreeInOrder(pHead,0);
	printf("\nprintTreePreOrder:\n");
	printTreePreOrder(pHead);
	printf("\nprintTreePostOrder:\n");
	printTreePostOrder(pHead);
	printf("\nHead node value: %d\n", pHead->variable);
	
/*	
	while(1)
	{
		printf("1. Add Node\n"); //1-9
		scanf("%d", &choice);
		if((choice < 9) && (choice > -1))
		{
			switch(choice)
			{
				case 0:
					return;
				case 1:
					pHead = AddNode(pHead);
					break;
				case 2:
					PrintTree(pHead);
					break;
				default:
					printf("Invalid choice entered! Try again\n");
					break;				
			}
		}
		
	}
*/
}
