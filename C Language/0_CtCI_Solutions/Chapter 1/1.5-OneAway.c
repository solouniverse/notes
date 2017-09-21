//SriMatreNamaha!
/*
 * One Away: Write a method to check if they are one edit away.
 * Ex:	pale, ple	-> True
 * 		pales, pale	-> True
 * 		pale, bale	-> True
 * 		pale, bake	-> False
 * 
 * Logic: Check the total count of each character from the biggest string 
 * 			in both strings if only one the characters are less by 1 char.
 * 			its a True otherwise not.
 * Algorithm:
 *	1. Check the length of both strings if they are only apart by 1 char.
 * 	2. Take the biggest string as string1 2nd one as string2.
 * 	3. Take one character from string1 and find total occurances of it in string1
 * 	4. Count the same with string2.
 * 	5. If they are differ by 1:
 * 		a. Notedown it as 'missing char' if its the first of this kind. 
 * 						(or)
 * 		b. Throw error if it doesnt match with 'missing char' already found.
 *	6. If they are differ by more than 1, throw error and exit.
 * 	7. Repeat steps 1-6 till biggest string ends.
 * 	8. Declare the string pair as '1 edit away' if it reaches here.
 * 
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
	char strString1[100], strString2[100], chMissingChar='\0';
	char * pstrString1, * pstrString2;
	int i, j, iCount1=0, iCount2=0;
	
	printf("Enter String 1:");
	scanf("%s",strString1);
	
	printf("Enter String 2:");
	scanf("%s",strString2);
	
	iCount1=strlen(strString1);
	iCount2=strlen(strString2);
	
	/*1. Check the length of both strings if they are only apart by 1 char.*/
	if( !( (iCount1 == iCount2) || (iCount1 == iCount2+1) || (iCount1 == iCount2-1) ) )
	{
		printf("Length difference is beyond 1 character. Cannot be 1 edit away strings.\n");
		exit(0);
	}
	/* 	2. Take the biggest string as string1 2nd one as string2.*/
	if( iCount1 > iCount2 )
	{
		pstrString1=strString1;
		pstrString2=strString2;
	}
	else
	{
		pstrString2=strString1;
		pstrString1=strString2;
	}

	for (i=0; pstrString1[i] != '\0'; i++)
	{
		/*	3. Take one character from string1 and find total occurances of it in string1*/
		for (iCount1=0,j=0; pstrString1[j] != '\0'; j++)
		{
			if (pstrString1[j] == pstrString1[i])
			{
				iCount1++;
			}
		}
		/*4. Count the same with string2.*/
		for (iCount2=0,j=0; pstrString2[j] != '\0'; j++)
		{
			if (pstrString2[j] == pstrString1[i])
			{
				iCount2++;
			}
		}

		//printf("pstrString1[i]='%c', iCount2=%d, iCount1=%d \n", pstrString1[i], iCount2, iCount1 );
		
		/* 	5. If they are differ by 1: */
		if( (iCount2 == iCount1+1) || (iCount2 == iCount1-1) )
		{
			/*	5a. Notedown it as 'missing char' if its the first of this kind.*/
			if ('\0' == chMissingChar)
			{
				chMissingChar = pstrString1[i];
			}
			/*	5b. Throw error if it doesnt match with 'missing char' already found.*/
			else if (chMissingChar != pstrString1[i])
			{
				printf("More than 1 characters are missing:'%c','%c'\n",chMissingChar, pstrString1[i]);
				exit(0);
			}
		}
		/*	6. If they are differ by more than 1, throw error and exit.*/
		else if(iCount2 != iCount1)
		{
			printf("'%c' character is missing more than once cannot be 1 edit away strings.\n", pstrString1[i]);
		}
	}/*	7. Repeat steps 1-6 till biggest string ends.*/
	
	/*	8. Declare the string pair as '1 edit away' if it reaches here.*/
	printf("'%s', '%s' are 1 edit apart with '%c'\n", strString1, strString2, chMissingChar);
}

/*
 * Output:
 * 
[2017-09-17 16:26.25]  /drives/d/W/Learning/0_CtCI
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Enter String 1:aaa
Enter String 2:aa
'aaa', 'aa' are 1 edit apart with 'a'
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[2017-09-17 16:26.30]  /drives/d/W/Learning/0_CtCI
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Enter String 1:abad
Enter String 2:aba
'abad', 'aba' are 1 edit apart with 'd'
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[2017-09-17 16:26.42]  /drives/d/W/Learning/0_CtCI
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Enter String 1:aba
Enter String 2:aa
'aba', 'aa' are 1 edit apart with 'b'
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[2017-09-17 16:26.50]  /drives/d/W/Learning/0_CtCI
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Enter String 1:aaaaaaaaacf
Enter String 2:aaaacfaaaaaa
'aaaaaaaaacf', 'aaaacfaaaaaa' are 1 edit apart with 'a'
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
*/
