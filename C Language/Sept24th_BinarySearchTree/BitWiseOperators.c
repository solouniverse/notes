//SriMatreNamah
#include <stdio.h>

void printBits(unsigned int iNumber)
{
	unsigned int mask, count=0;
	
	mask=1<<(sizeof(int)*8-1);
	//printf("%13d: ",iNumber);
	//printf("%13x: ",iNumber);
	while(mask){
		if(iNumber&mask)
			printf("1");
		else
			printf("0");
			
		mask=mask>>1;
		count++;
		if(count%8 == 0)
			printf(" ");
/*
		if(count%8 == 0)
			printf("|");
		else if(count%4 == 0)
			printf(" ");
*/		
	}
	printf("\n");
}

void checkLshiftRshift(void)
{
	int iNumber=31;
	for (int i=0;i<32;i++)
	{
		if(i<10)
			iNumber=iNumber<<1;
		else
			iNumber=iNumber>>1;
			
		printBits(iNumber);		
	}
}

void main(void)
{
	unsigned int number, mask;
/*	
	number=21;
	mask = 31<<2;
	printf("number|mask:\n");
	printBits(number);
	printBits(mask);
	printBits(number|mask);

	printf("number&mask:\n");
	printBits(number);
	printBits(mask);
	printBits(number&mask);

	printf("number^mask:\n");
	printBits(number);
	printBits(mask);
	printBits(number^mask);

	printf("~0:\n");
	printBits(~0);
	
	printf("~0<<8:\n");
	printBits(~0<<8);
	
	printf("(1<<17)\n");
	printBits((1<<17));
	printf("~(1<<17)\n");
	printBits(~(1<<17));
	
	printf("To check if a number perfect 2^x or not\n");
	number=32;
	printf("%d&(%d-1)\n",number,number);
	printBits(number);
	printBits(number-1);
	printBits(number&(number-1));
	
	number=1024;
	printf("%d&(%d-1)\n",number,number);
	printBits(number);
	printBits(number-1);
	printBits(number&(number-1));
	
	number=1000;
	printf("%d&(%d-1)\n",number,number);
	printBits(number);
	printBits(number-1);
	printBits(number&(number-1));
	
	number=31;
	printf("%d&(%d-1)\n",number,number);
	printBits(number);
	printBits(number-1);
	printBits(number&(number-1));
	
	if(number&(number-1) == 0)
		printf("Its a perfect 2^x\n");
	
	for(i=0;i*i<=number;i++)
		continue;
		
	if(i*i == number)
		printf("Its a perfect 2^x\n");
*/	
	//printBits((1<<31)<<4);
	printBits(1021);
}
