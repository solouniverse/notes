//SriMatreNamah!
#include <stdio.h>
#include <malloc.h>

typedef struct node {
	int value;
	struct node *link;
} Node;

struct node * getNode(void)
{
	struct node * temp;
	temp=malloc(sizeof(struct node));
	if (temp != NULL){
		printf("\nEnter value for new node: ");
		scanf("%d", &temp->value);
		temp->link=NULL;
	}
	else
		printf("Failed to allocate memory for newnode!%s:%d",__func__,__LINE__);
	return temp;
}

struct node * addNode( struct node *head)
{
	struct node *temp=NULL;
	if(NULL == head)
	{
		printf("List is empty adding first node!");
		head=getNode();
	}
	else
	{	
		temp=head;
		while(NULL != temp->link)
		{
			temp=temp->link;
		}
		temp->link = getNode();
	}
	return head;
}

struct node * pop( struct node *head)
{
	struct node *temp=head;
	struct node *tempPrev=NULL;
	if(NULL == head)
	{
		printf("List is empty ");
	}
	else
	{	
		if (NULL == temp->link )
		{
			printf("Deleting node with value %d\n",temp->value);
			free(temp);
			head=NULL;
		}
		else
		{
			while(NULL != temp->link)
			{
				tempPrev=temp;
				temp=temp->link;
			}
			printf("Deleting node with value %d\n",temp->value);
			free(temp);
			tempPrev->link=NULL;
		}
	}
	return head;
}

void printList(struct node *head)
{
	struct node *temp=head;
	if(NULL != temp){
		do
		{
			printf("%d ",temp->value);
			temp=temp->link;
		}while(NULL != temp);
	}
	else
	{
		printf("List is empty nothign left for deletion!\n");
	}
}

void printListReverse(struct node *head)
{
	if(NULL != head){
		printListReverse(head->link);
		printf("%d ",head->value);
	}
}

Node * ListReverse(Node * current, Node * prev)
{
	Node * temp;
	if(NULL != current){
		temp = ListReverse(current->link, current);
		current->link = prev;
		return temp;
	}else{
		return prev;
	}
}

int main()
{
	struct node *head=NULL;
	int choice;
	
	while(1){
		printf("\n1.Push\n2.Pop\n3.Print Reverse\n4.Print\n5.Reverse the list\n0.Exit\n");
		printf("Enter stack operation:");
		scanf("%d", &choice);
		if(choice > -1 && choice < 9){
			switch(choice){
				case 1:
					head=addNode(head);
					break;
				case 2:
					head=pop(head);
					break;
				case 3:
					if(NULL != head)
						printListReverse(head);
					else
						printf("Cannot reverse empty string!\n");
					break;
				case 4:
					printList(head);
					break;
				case 5:
					head=ListReverse(head, NULL);
					break;
				case 0:
					return 0;
				default:
					printf("\nInvalid option!!");
					break;
			}
		}else{
			printf("\nInvalid option!!");
		}		
	}
}

