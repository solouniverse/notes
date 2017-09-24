#include <stdio.h>
#include <malloc.h>
#define MAX 5
struct DoubleNode {
	struct DoubleNode * pLinkL;
	struct DoubleNode * pLinkR;
	int variable;
};
typedef struct DoubleNode DNode;

void PrintDoubleList(DNode * head)
{
	printf("From %s ____\n",__func__);
	while(head != NULL){
		printf("%d > ", head->variable);
		head = head->pLinkR;
	}
}

void deleteNode(DNode * pHead, int ikey)
{
	int iCount=0;
	DNode * pTemp, *pTempPrev;
	printf("From %s ____\n",__func__);
	pTemp=pHead;
	while((pTemp != NULL) && (pTemp->variable != ikey)){
		pTempPrev=pTemp;
		pTemp = pTemp->pLinkR;
	}

	if(pTemp->variable == ikey){
		pTempPrev->pLinkR =  pTemp->pLinkR;
		free(pTemp);
		printf("Deleted Node with key\n",ikey);
	}else
		printf("Key not found!\n");	
}

void FindKey(DNode * pHead, int ikey)
{
	int iCount=0;
	printf("From %s ____\n",__func__);
	while((pHead != NULL) && (pHead->variable != ikey)){
		pHead = pHead->pLinkR;
		iCount++;
	}
	if(pHead->variable == ikey)
		printf("found %d at %u\n",ikey, iCount);
	else
		printf("Key not found!\n");
	
}

void FindValueReverseIndex(DNode * pHead, int Index)
{
	int iCount=1;
	DNode * pTemp=NULL;
	DNode * pTemp2=NULL;
	printf("From %s ____\n",__func__);
	
	pTemp = pHead;
	
	while(pTemp != NULL){	
			
		if(iCount == Index)
		{
			pTemp2 = pHead;
		}
		else if(iCount > Index)
		{
			pTemp2=pTemp2->pLinkR;
		}
	
		iCount++;
		pTemp = pTemp->pLinkR;		
	}
	if(pTemp2 != NULL)
		printf("%d index from end is:\t'%d'\n",Index, pTemp2->variable);
	else
		printf("List is shorter than index!\n");
	
}

int FindValueReverseIndexRecursive(DNode * pHead, int Index)
{
	int iCount;
	if(pHead == NULL)
		return 1;
	else{
		iCount=FindValueReverseIndexRecursive(pHead->pLinkR, Index);
		if(iCount == Index){
			printf("From %s ____\n",__func__);
			printf("%d index from end is:\t'%d'\n",Index, pHead->variable);
		}
		return(iCount+1);
	}
}

void FindKeyFromEnd(DNode * pHead, int ikey)
{
	int iCount=0;
	int iCountTotal=0;
	DNode * pTemp;
	pTemp = pHead;
	
	printf("From %s ____\n",__func__);
	while((pTemp != NULL) && (pTemp->variable != ikey)){
		pTemp = pTemp->pLinkR;
		iCount++;
	}
	
	pTemp = pHead;	
	while((pTemp != NULL)){
		pTemp = pTemp->pLinkR;
		iCountTotal++;
	}
	
	if(iCount)
		printf("The distance of value %d at from the end is %u\n",ikey, iCountTotal-iCount);
	else
		printf("Key not found!\n");
}

void PrintListReverse(DNode * pHead)
{
	if((pHead != NULL)){
		PrintListReverse(pHead->pLinkR);
		printf(" < %d", pHead->variable);
	}
}

void PrintListReverseUsingTail(DNode * pTail)
{
	printf("From %s ____\n",__func__);
	while(pTail != NULL){
		printf("%d > ", pTail->variable);
		pTail = pTail->pLinkL;
	}
}

/*
int FindIntersection(DNode * head)
{
	Node * pHead;
	Node * pHead2;
	
	int CircularFound=0;
	
	pHead=head;
	pHead2 = pHead->pi;
	
	while((pHead != NULL) && (pHead2 != NULL)){
		if ( pHead == pHead2){
				printf("Found a circular link @%u:%u\n", pHead,pHead2);
				return(1);
		}
		pHead = pHead->pi;
		pHead2 = (Node *)(pHead2->pi)->pi;
	}

	//Under development

	for (i=0;i<j;i++)
	{
		if((pHead2->pi != NULL))
			pHead2 = pHead2->pi;;
		else
			break;
	}
	return(0);
}
*/

int GetLengthOfList(DNode * head)
{
	int iCount=0;
	printf("From %s ____\n",__func__);
	while(head != NULL){
		iCount++;
		head = head->pLinkR;
	}
	return iCount;
}

/*
void isListPalindrome(DNode *pHead)
{
	int LengthOfList, isPalindrome=1, i;
	LengthOfList= GetLengthOfList(pHead);
	for (i=1;i<LengthOfList;i++)
	{
		if(FindValueReverseIndex(pHead, i) != FindValueReverseIndexRecursive(pHead, i)){
			isPalindrome=0;
			break;
		}
	}
	if(isPalindrome)
		printf("List is a palindrome !!\n");
	else
		printf("List isn't a palindrome\n");
}
*/

int GetReverseNumberFromList(DNode * pHead)
{
	int iNumber;
	if(pHead == NULL){
		printf("From %s ____\n",__func__);
		return 0;
	}else{
		iNumber=GetReverseNumberFromList(pHead->pLinkR);
		return(iNumber*10+pHead->variable);
	}
}

int GetNumberFromList(DNode * head)
{
	int iNumber=0;
	printf("From %s ____\n",__func__);
	while(head != NULL){
		iNumber=iNumber*10+head->variable;
		head = head->pLinkR;
	}
	printf("Number from List is: %d", iNumber);
	return iNumber;
}

void isNumberPalindrome( int iNumber)
{
	int iPalindrome=0, iTempNumber;
	iTempNumber=iNumber;
	while(iTempNumber !=0)
	{
		iPalindrome=iPalindrome*10+iTempNumber%10;
		iTempNumber/=10;
	}
	
	if(iNumber == iPalindrome)
		printf("%d is a Palindrome\n", iNumber);
	else
		printf("%d is **NOT** aPalindrome\n", iNumber);
}

int main(void)
{
	int iIntValues[MAX] = {1,2,3,4,1};
	DNode *pHead=NULL;
	DNode *pTemp=NULL;
	DNode *pTail=NULL;
	int i;
	
	for(i=0;i<MAX;i++){
		pTemp = malloc(sizeof(DNode));
		if(pTemp != NULL)
		{
			pTemp->variable = iIntValues[i];
			pTemp->pLinkL = NULL;
			pTemp->pLinkR = NULL; // List will be circular if 'pHead' is assigned instead of 'NULL' 
		}else{
			printf("Failed to allocate memory of %d bytes!\n", sizeof(DNode));
			return -1;
		}
		if(pHead == NULL){
			pHead=pTemp;
			pTail=pTemp;
		}else{
			pTail->pLinkR = pTemp;
			pTemp->pLinkL = pTail;
			pTail = pTail->pLinkR;
		}
	}
	PrintDoubleList(pHead);
	printf("\n------------------------------------------------\n");
	PrintListReverse(pHead);
/*
	PrintListReverseUsingTail(pTail);
	printf("\n------------------------------------------------\n");
	FindKey(pHead, 33);
	printf("\n------------------------------------------------\n");
	FindKeyFromEnd(pHead, 33);
	printf("\n------------------------------------------------\n");
	FindValueReverseIndex(pHead, 1);
	printf("\n------------------------------------------------\n");
	FindValueReverseIndexRecursive(pHead, 3);
*/
	printf("\n------------------------------------------------\n");
/*	isListPalindrome(pHead);
*/	isNumberPalindrome(GetReverseNumberFromList(pHead));
	GetNumberFromList(pHead);	

	deleteNode(pHead, 3);
	printf("\n------------------------------------------------\n");
	PrintDoubleList(pHead);
}

void swapTwoNodes()
{
	ptPrev=pTemp;
	pTemp=pTemp->pLinkR;

	ptPrev=pTemp->pLinkR;
	pTemp2=*(pTemp->pLinkR)->pLinkR;
	*(ptPrev->pLinkR)->pLinkR=pTemp;
	pTemp->pLinkR=pTemp2;
}





