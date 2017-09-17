/*
 * Palindrome Permutation:
 * Ex: i/p tact cao
 * "taco cat", "atco cta"
 * 
 * */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char str[100], odd_char='\0';
	int i, j, len, odd_count=0, count=0;
	
	printf("Enter string: ");
	scanf("%s", str);
	len=strlen(str);
	
	for ( i=0 ; str[i] != '\0' ; i++)
	{	
		count=0;
		for ( j=0 ; str[j] != '\0' ; j++)
		{
			if(str[i] == str[j]){
				count++;
			}
		}
		
		if (count%2 != 0 )
		{
			if (odd_char == '\0')
			{
				odd_char=str[i];
			}
			else if (odd_char != str[i])
			{
				printf("1. str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
				printf("'%s' cannot be a polindrome!\n", str);
				exit(0);
			}
			odd_count++;
		}
		
		if (( len%2 == 0 ) && ( odd_count > 0))
		{
			printf("2. str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
			printf("'%s' cannot be a polindrome!\n", str);
			exit(0);
		}
	}
	if (( len%2 != 0 ) && ( odd_count%2 == 0))
	{
		printf("3. str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
		printf("'%s' cannot be a polindrome!\n", str);
		exit(0);
	}

	printf("Its a palindrome\n");
	printf("str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
}




