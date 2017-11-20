#include <stdio.h>

int isPositive_v1(int N)
{
//Use logical operation to find sign
	return(N>0);
}

int isPositive(int N)
{
//for all int's MSB is sign bit. sign bit=1 if -ve, =0 if +ve 
	return((unsigned int)N>>((sizeof(int)*8)-1));
}

int my_abs(int n)
{
	int mask=~(1<<(sizeof(int)*8)-1);
//If n<0 clear sign bit and caliculate reverse 2's complement of it.  
	if(n<0)
		return(~(n-1) & mask);
//If n>0 return as it is.
	return(n);
}

int my_abs_2(int n)
{
	int mask=~(1<<(sizeof(int)*8)-1);

//		return(~(n-1) & mask);
	
	//sign_bit 1 => -ve
	//return((-ve)|(+ve));
	//return((-ve)| (pMask) & (n) );
}

int my_abs_3(int n)
{
	int mask=~(1<<(sizeof(int)*8)-1);
	unsigned int sign_bit=(unsigned int)n>>(sizeof(int)*8-1);
	unsigned int pMask=~0+sign_bit; //FFF if n>0; 0 if n<0
	// Below logic selects right value from 2 inputs w/o using if-else
	//Logic:use some mask to make one side '0' when its not valid and 
	//		use its complement on the other side and bitwise or them.
	return((pMask & n) | (~pMask & ( ~(n-1) & mask ) ) );
}

int my_max(int n, int m)
{
	int sign_bit =(unsigned int)(n-m)>>(sizeof(int)*8-1);
	// Below logic selects right value from 2 inputs w/o using if-else
	//Logic:Use some mask to make one side '0' when its not valid and 
	//		use its complement on the other side and bitwise or them.
	//Find max: for all n,m; n-m will be -ve if n<m and vice-versa. 
	return( (~0+sign_bit)&n|(~(~0+sign_bit)&m) );
}

int my_max_2(int n, int m)
{
	int mask=~0+(n<m);
	//Find max: ~0=FFFF.. ,
	//	if n<m,(n<m)=>1,then ~0+(n<m)=>0,then (mask&n | ~mask&m)=>m
	//	if n>m,(n<m)=>0,then ~0+(n<m)=>FF..F,,then (mask&n | ~mask&m)=>n

	return(mask&n | ~mask&m);
}

int my_min(int n, int m)
{
	// Do the same as above using the sign bit.
	int sign_bit =(unsigned int)(n-m)>>(sizeof(int)*8-1);
	return( (~0+sign_bit)&m|(~(~0+sign_bit)&n) );
}

void main(void)
{
	printf("%d\n",isPositive(1024));
	printf("%d\n",isPositive(-1024));
	return;
	for(int x=0, y=-5;y < 5;y++){
		//printf("%d:%d\n",y,y ^ ((x ^ y) & -(x < y)));
		printf("%d:%d\n",y,my_max_2(x,y)); 
	}
	return;

	return;
	printf("%u\n",~((-2+1)^1 -1)); 
	printf("%u\n",~((-2^1)-1 -1)); 
	printf("%d\n",my_abs(1024)); 
	printf("%d",my_abs(-1024)); 
}


void printf_in_if(void)
{	
	printf("printed %d\n",printf("from if\n"));
	if(!printf("from if\n"))
		printf("from if\n");
	else
		printf("from else\n");
}

int mains(void)
{
	char *cP=NULL;
	int i=-1, *iP;
	iP=&i;
	cP=(char*)&i;
	printf("size of int:%u\n", sizeof(int));
	printf("Using int pointer: %d\n", *iP);
	for(int k=0; k<sizeof(int)*8;k++){
		for( int j=0;j<sizeof(int);j++){
			printf(" %", *(cP+j));
		}
		i=i<<1;
		printf("\n");
	}
}
