
#include <stdio.h>

int main(void)
{
	char *cP=NULL;
	int i=1, *iP;
	iP=&i;
	cP=(char*)&i;
	printf("size of int:%u\n", sizeof(int));
	printf("Using int pointer: %d\n", *iP);
	for(int k=0; k<sizeof(int)*8;k++){
		for( int j=0;j<sizeof(int);j++){
			printf(" %i", *(cP+j));
		}
		i=i<<1;
		printf("\n");
	}
}

int main_2(void)
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
		printf("%d,%u\n",*(a+i),(a+i));
	}
	printf("-----\n");
	for(int i=0;i<9;i++){
		printf("%d,%u\n",p[i],&p[i]);
	}
	printf("-----\n");
	for(int i=0;i<9;i++){
		printf("%d,%u\n",*(p+i),(p+i));
	}
	printf("Size of int is:%d", sizeof(int));
}



