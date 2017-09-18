//SriMatreNamaha!
/*
 * Implement a method to perform basic string compression using the 
 * 		counts of repeated characters.
 * Ex:
 * 		aaabbbccc -> a3b3c3
 * 		aaaaaaaaaaaabbaaabbaaaaabac -> a12b2a3b2a5b1a1c1
 * 
 */
#include <stdio.h>
#include <string.h>
int main()
{
	char strString[100];
	int i,j, iLen, iCount;
	printf("Enter string to be compressed: ");
	scanf("%s", strString);
	iLen=strlen(strString);
	
	for (i=0; i<iLen; i++)
	{
		iCount=0;
		for (j=i; j<iLen && (strString[i] == strString[j]); j++)
		{
			iCount++;
		}
		i=j-1;
		printf("%c%d",strString[i],iCount);
	}
}
