#include <stdio.h>
#define MAX 3

void printArray_or_Horizontal(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[i][j]);
		}
		printf("\n");
	}
}

void printArrayTopDown_or_Vertical(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[j][i]);
		}
		printf("\n");
	}
}

void printArrayUpsideDown_or_HorizontalFlip(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[MAX-i-1][j]);
		}
		printf("\n");
	}
}

void printArrayRightToLeft_or_VerticalFlip(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[i][MAX-1-j]);
		}
		printf("\n");
	}
}

void printArray_Rotate_90(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[MAX-1-j][i]);
		}
		printf("\n");
	}
}

void printArrayRightToLeftUpsideDown_or_Rotate_180(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[MAX-1-i][MAX-1-j]);
			//printf("%d \t",piArray[MAX-1-j][MAX-1-i]);
		}
		printf("\n");
	}
}

void printArrayprintArrayVerticalUpsideDown_Rotate_270(int piArray[MAX][MAX])
{
	int i,j;

	printf("\n%s:\n", __func__);
	for (i=0;i<MAX;i++)
	{
		for (j=0;j<MAX;j++)
		{
			printf("%d \t",piArray[j][MAX-1-i]);
		}
		printf("\n");
	}
}

int main()
{
	int iArray[MAX][MAX]={{1,2,3},{4,5,6},{7,8,9}};
	
	printArray_or_Horizontal(iArray);
	printArrayTopDown_or_Vertical(iArray);
	printArrayUpsideDown_or_HorizontalFlip(iArray);
	printArrayRightToLeft_or_VerticalFlip(iArray);
	printArray_Rotate_90(iArray);
	printArrayRightToLeftUpsideDown_or_Rotate_180(iArray);
	printArrayprintArrayVerticalUpsideDown_Rotate_270(iArray);
}
