//SriMatreNamaha

#include <stdio.h>
#include <stdlib.h>
#define INIT_DA_SIZE 5

struct dynamic_array{
	int *ipDA;
	int size; //number of items
	int capacity; //number of items it can hold
};

void display_DA(struct dynamic_array *);

int array_example(void)
{
	int a[]={123,121,234,1,2,3,11,22,33};
	int *p;
	//p=&a[0];
	p=a;
	for(int i=0;i<9;i++){
		printf("%d,%u\n",a[i],&a[i]);
	}
	printf("-----\n");
	for(int i=0;i<9;i++){
		printf("%d,%u\n",p[i],&p[i]);
	}
	printf("Size of int is:%d", sizeof(int));
}

void resize_DA(struct dynamic_array *DA, size_t size)
{
	DA->ipDA=malloc(size * sizeof(int));
	if(DA->ipDA == NULL)
	{
		printf("failed to allocate memory\n");
		exit(0);
	}
	DA->capacity += size;
	printf("Current capacity: %d\n", DA->capacity);
}

struct dynamic_array * create_DA(size_t size){
	struct dynamic_array * tempP;
	
	tempP=malloc(sizeof(struct dynamic_array));
	tempP->ipDA=NULL;
	tempP->size=0;
	tempP->capacity=0;

	resize_DA(tempP, size);

	return(tempP);
}

void expand(struct dynamic_array *DA)
{
	int * tempP=NULL;
	//printf("DA is exteneding to %d\n", DA->capacity*2);
	
	tempP=malloc(DA->capacity * 2 * sizeof(int));
	for(int i=0; i< DA->size; i++){
		tempP[i]=DA->ipDA[i];
	}
	DA->capacity=DA->capacity*2;
	printf("DA is exteneded to %d\n", DA->capacity);
	free(DA->ipDA);
	DA->ipDA=tempP;
}

void shrink(struct dynamic_array *DA)
{
	int * tempP=NULL;
	//printf("DA is shrinking to %d\n", DA->capacity*2);
	
	tempP=malloc(DA->capacity / 2  * sizeof(int));
	for(int i=0; i< DA->size; i++){
		tempP[i]=DA->ipDA[i];
	}
	DA->capacity=DA->capacity/2;
	printf("\nDA is shrinked to %d\n", DA->capacity);
	free(DA->ipDA);
	DA->ipDA=tempP;
}

void push_DA(struct dynamic_array *DA, int data)
{
	if(DA->size >= DA->capacity ){
		expand(DA);
	}
	DA->ipDA[DA->size]=data;
	DA->size++;
}

int pop_DA(struct dynamic_array *DA)
{
	if(DA->size <= 0){
		return 0;
	}
	if (DA->size < DA->capacity/4){
		shrink(DA);
	}
	DA->size--;
	return(DA->ipDA[DA->size]);
}

void display_DA(struct dynamic_array *DA)
{	
	if(!DA->size){
		printf("Dynamic array is empty!\n");
		return;
	}
	for(int i=0; i<DA->size;i++){
		printf("%d ",DA->ipDA[i]);
	}
	printf("\n");
}

int find(struct dynamic_array *DA, int data)
{
	for(int i=0; i<DA->size;i++)
	{
		if(DA->ipDA[i] == data)
		return i;
	}
	return -1;
}

int is_empty(struct dynamic_array *DA)
{
	return !DA->size;
}

void insert(struct dynamic_array *DA, int index, int data)
{
	if(index > DA->size)
	{
		printf("Index is outof range\n");
		return;
	}
	if(index == DA->size)
	{
		push_DA(DA, data);
	}
	else
	{
		insert(DA, index+1, DA->ipDA[index]);
		DA->ipDA[index]=data;
	}	
}

void delete(struct dynamic_array *DA, int index)
{
	if(index >= DA->size)
	{
		printf("Index is outof range\n");
		return;
	}
	for(int i=index; i<DA->size;i++)
	{
		DA->ipDA[i]=DA->ipDA[i+1];
	}
	pop_DA(DA);
}

int remove_item(struct dynamic_array *DA, int data)
{
	int index;
	while(1){
		index=find(DA, data);
		if(index >=0)
		{
			delete(DA, index);
		}
		else
		{
			printf("%d is not found in DA\n", data);
		}
		return(index);
	}
}

void remove_item_all(struct dynamic_array *DA, int data)
{
	int index;
	while(1){
		index=find(DA, data);
		if(index < 0)
			return;
		delete(DA, index);		
	}
}

void remove_item_all_2(struct dynamic_array *DA, int data)
{
	while(1){
		if(remove_item(DA, data) < 0)
			return;
	}
}

void main(void){
	struct dynamic_array *myDA;
	
	myDA=create_DA(INIT_DA_SIZE);
	
	for(int i=0; i<20;i++){
		push_DA(myDA,i*11);
	}
	
	display_DA(myDA);
	printf("%d\n",find(myDA,36));
	printf("%d \n",myDA->size);
	printf("%d\n",remove_item(myDA,44));
	display_DA(myDA);
	printf("%d \n",myDA->size);
	return;
	//printf("%d \n",pop_DA(myDA));
	printf("%d \n",myDA->size);
	insert(myDA,5,1111);
	display_DA(myDA);
	printf("%d \n",myDA->size);
	insert(myDA,21,1001);
	display_DA(myDA);
	printf("%d \n",myDA->size);
	for(int i=myDA->size; i>2;i--){
		delete(myDA,1);
	}
	display_DA(myDA);
	printf("%d \n",myDA->size);
	return;
	for(int i=myDA->size; i>0;i--){
		printf("%d ",pop_DA(myDA));
	}
}
