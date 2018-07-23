#include <stdio.h>
#define A_MAX 4

void buildArray(int a[A_MAX][A_MAX])
{
	for (int i=0; i<A_MAX; i++)
	{
		for (int j=0; j<A_MAX; j++)
		{
			a[i][j] = i*A_MAX+j;
		}
	}
}

void printArray(int a[A_MAX][A_MAX])
{
	for (int i=0; i<A_MAX;i++)
	{
		for (int j=0; j<A_MAX; j++)
		{
			printf("%2d ", a[i][j]);
		}
		printf("\n");
	}
	printf("------------------------------------------------\n");
}

void printArraySpiral (int a[A_MAX][A_MAX])
{
/* Prints a 2D array in spiral order.
 * Ex 1:
 * 0  1  2  3
 * 10 11 12 13
 * 20 21 22 23
 * 30 31 32 33
 * 
 * OutPut:
 * 0  1  2  3 13 23 33 32 31 30 20 10
 * 11 12 22 21
 * 
 * Ex 2:
 *  0  1  2  3  4  5
 * 10 11 12 13 14 15
 * 20 21 22 23 24 25
 * 30 31 32 33 34 35
 * 40 41 42 43 44 45
 * 50 51 52 53 54 55
 * 
 * OutPut:
 * 0  1  2  3  4  5 15 25 35 45 55 54 53 52 51 50 40 30 20 10
 * 11 12 13 14 24 34 44 43 42 41 31 21
 * 22 23 33 32 
 */
	int j=0, i=0, layer=0;

	for (; layer<=A_MAX/2; layer++)
	{
		j=i=layer;
		for (; j<A_MAX-layer; j++)
		{
			printf("%2d ", a[i][j]);
		}

		j--;
		i++;
		for (; i<A_MAX-layer; i++)
		{
			printf("%2d ", a[i][j]);
		}

		i--;
		j--;
		for (; j>=0+layer; j--)
		{
			printf("%2d ", a[i][j]);
		}

		i--;
		j++;
		for (; i>0+layer; i--)
		{
			printf("%2d ", a[i][j]);
		}
		printf("\n");
	}
}

void main (void)
{
	int a[A_MAX][A_MAX];
	buildArray(a);
	printArray(a);
	printArraySpiral(a);
}
