//Sri matre namaha
/*
 * Write a method to replace all spaces in a string with '%20'. You may 
 * 		assume that the string has sufficent space at the end to hold 
 * 		the additional characters. 
 * Logic: 
 * 		1. Inplace replace:
 * 			a. Traverse through the string and find a space.
 * 			b. When a space is found duplicate the string after space into a temp string variable.
 * 			c. Insert '%','2','0' characters into the main string.
 * 			d. Now copy the backup copy of remaining string after space into main string.
 * 			e. Repeat steps a-d till the end of main string.
 *		2. ReplaceSpaces using a 2nd string:
 * 			a. Copy main string into 2nd string character by character.
 * 			b. If you find a space in main string add '%','2','0' characters into 2nd string and ignore space.
 * 			c. Repeat till end of main string is reached.
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ReplaceSpacesInPlace(char * strString)
{
	char * pStrTemp;
	unsigned i=0;

	while('\0' != strString[i]){
		/* When a space is found */
		if(' ' == strString[i]){
			/*duplicate the string after space into a temp string variable.*/
			pStrTemp=strdup(strString+i+1);
			/* Insert '%','2','0' characters into the main string. */
			strString[i++]='%';
			strString[i++]='2';
			strString[i++]='0';
			/* Now copy the backup copy of remaining string after space into main string. */
			strcpy(strString+i, pStrTemp);
			/* free the space allocated to temp string which is no longer need*/
			free(pStrTemp);
		}else{
			i++;
		}
	}
}

void ReplaceSpaces(char * strString, char * strString2)
{
	unsigned i=0, j=0;
	
	do{
		if(' ' == strString[i]){
		/* If you find space insert '%','2','0' instead of it */
			strString2[j++]='%';
			strString2[j++]='2';
			strString2[j++]='0';
		}else{
		/* For all other characters other than ' ' simple copy them*/
			strString2[j++]=strString[i];
		}
		/*Procede to next character in the input string and repeat*/
		i++; 
	}while('\0' != strString[i]); 
	/* Using do..while instead of for or while lets control over i,j and 
	 * 	copies '\0' at the end without much logic
	 */
}


int main (void)
{
	char strString[100];
	char strString2[100];
	
	printf("Enter string: ");
	/* 
	 *"%[^\n]" Read till end of line dont consider spaces as delimiters!
	 */
	scanf("%[^\n]",strString); 
	/* Adding '|' at the begining and end of string to recognise trailing spaces */
	printf("|%s|\n", strString); 
	ReplaceSpaces(strString, strString2);
	printf("|%s|\n", strString);
	printf("|%s|\n", strString2);
	ReplaceSpacesInPlace(strString);
	printf("|%s|\n", strString);
}



