/*
 * Palindrome Permutation:
 * Ex: i/p tact cao
 * "taco cat", "atco cta"
 * 
 * Logic: 
 * 1. In even lengthy palindrom all characters should present in even count only!
 * 2. In odd lengthy palindrom only one character can be repeated odd times 
 * 		all others characters should present in even count only!
 * 
 * */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEBUGGING 1
#undef DEBUGGING
#ifdef DEBUGGING
	#define DEBUG printf
#endif
#ifndef DEBUGGING
	#define DEBUG if(0) printf
#endif

/*
 *> This logic finds out odd repetitions of characters and verifies 2 \
 * 		conditions mentioned at the top of this program. 
 *> It doen't care about counting odd occurances of character but keeps 
 * 		track of those characters. A string not be a palindrome: 
 *		1. If odd occurances found in a even lenghty string.
 *		2. If more than 1 characters occured odd times even in a odd lengthy string.
 */
 
int is_PalindromePermutation_2(char *str)
{
	char odd_char='\0';
	int i, j, len, count=0;
	
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
				DEBUG("1. str[i]=%c,i=%d, len=%d \n", str[i], i, len);
				printf("'%s' cannot be a polindrome!\n", str);
				printf("More than 1 characters have odd repetition count!\n");
				return (0);
			}
		}
		
		if (( len%2 == 0 ) && (odd_char != '\0'))
		{
			DEBUG("2. str[i]=%c,i=%d, len=%d \n", str[i], i, len);
			printf("'%s' cannot be a polindrome!\n", str);
			printf("In a even length Polindrome all characters should have only even repetitions\n");
			return (0);
		}
	}
	
/*	
 * This condition never occures!
	if (( len%2 != 0 ) && (odd_char == '\0'))
	{
		DEBUG("3. str[i]=%c,i=%d, len=%d \n", str[i], i, len);
		printf("'%s' cannot be a polindrome!\n", str);
		printf("In a odd length Polindrome atleast one characters should have odd number of repetitions\n");
		return (0);
	}
*/
	printf("Its a palindrome\n");
	DEBUG("4. str[i]=%c,i=%d, len=%d \n", str[i], i, len);
	return (1);
}

/*
 * This logic finds out odd repetitions of characters and verifies 2 
 * conditions mentioned at the top of this program. 
 * It uses count of odd characters and decides based on it.
 * Also verifies number of odd characters (If odd characters >1 in an 
 * 		odd lengthy string it cannot be a palindrome)
 */
 
int is_PalindromePermutation(char *str)
{	
	char odd_char='\0';
	int i, j, len, odd_count=0, count=0;
	
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
				DEBUG("1. str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
				printf("'%s' cannot be a polindrome!\n", str);
				return (0);
			}
			odd_count++;
		}
		
		if (( len%2 == 0 ) && ( odd_count > 0))
		{
			DEBUG("2. str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
			printf("'%s' cannot be a polindrome!\n", str);
			return (0);
		}
	}
	if (( len%2 != 0 ) && ( odd_count%2 == 0))
	{
		DEBUG("3. str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
		printf("'%s' cannot be a polindrome!\n", str);
		return (0);
	}

	printf("Its a palindrome\n");
	DEBUG("str[i]=%c,i=%d, odd_count=%d , len=%d \n", str[i], i, odd_count, len);
	return (1);
}

int main()
{
	char str[100], odd_char='\0';
	int i, j, len, odd_count=0, count=0;
	
	printf("Enter string: ");
	scanf("%s", str);
	is_PalindromePermutation(str);
	is_PalindromePermutation_2(str);
}
