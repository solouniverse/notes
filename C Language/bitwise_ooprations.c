#include <stdio.h>

int isPositive_v1(int N)
{
	return(N>0);
}

int isPositive(int N)
{
	return(!N>>((sizeof(int)*8)-1));
}

int my_abs(int n)
{
	int mask=~(1<<(sizeof(int)*8)-1);
	if(n<0)
		return(~(n-1) & mask);
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

	return((pMask & n) | (~pMask & ( ~(n-1) & mask ) ) );
}

int my_max(int n, int m)
{
	int sign_bit =(unsigned int)(n-m)>>(sizeof(int)*8-1);
	return( (~0+sign_bit)&n|(~(~0+sign_bit)&m) );
}

int my_max_2(int n, int m)
{
	int mask=~0+(n<m);
	return(mask&n | ~mask&m);
}

int my_min(int n, int m)
{
	int sign_bit =(unsigned int)(n-m)>>(sizeof(int)*8-1);
	return( (~0+sign_bit)&m|(~(~0+sign_bit)&n) );
}

void main(void)
{
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
