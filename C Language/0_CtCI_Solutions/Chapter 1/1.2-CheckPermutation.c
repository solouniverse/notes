//SriMatreNamah!
/*
 * Given two strings. write a method to decide if one is permutation of other.
 * 
 * Logic: Check if each character has same number of repetitions in both strings.
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv)
{
	char *str1="SriSitaRamdu", *str2="SriRamaSitaa";
	char *ch;
	short i,j, count1, count2;
	
	/* Both lenghts should be same to become permutations of each other. */
	if (strlen(str1) != strlen(str2))
	{
		printf("Strings are not same in length. Cannot be permutations!\n");
		printf("%s, %s", str1, str2);
		exit(0);
	}
	
	//STEP 1: Take 1 character at a time from first string.
	for(i=0; str1[i] != '\0'; i++) 
	{
		//STEP 2: Count how many times it occured in first string.
		count1=0;
		for(j=0; str1[j] != '\0'; j++)
		{
			if(str1[i] == str1[j])
			{
				count1++;
			}
		}
		//STEP 3: Now count how many times it occured in second string.
		count2=0;
		for(j=0; str2[j] != '\0'; j++)
		{
			if(str1[i] == str2[j])
			{
				count2++;
			}
		}
		
		//STEP 4: Check if both are equal otherwise throw error and exit!
		if (count2 != count1)
		{
			printf("Strings are not permutation of other\n");
			exit(0);
		}
		//STEP 5: If both are equal goto STEP 1 and repeat with next character.
	}
	
	//STEP 6: If no more characters left in first string for comparision 
	//		it means both are permutation of each other.
	printf("Strings are permutation of other!!\n");
}
