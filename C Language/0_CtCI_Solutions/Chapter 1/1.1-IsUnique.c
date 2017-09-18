//SriMatreNamaha!
/*
 * Implement an algorithm to determine if a string has all unique 
 * characters. What if you cannot use additional datastructes?
 *  
 */

#include <stdio.h>
#include <string.h>

int determine_if_a_string_2(char *str)
{
	char ch, ch2;
	short found_flag = 1;
	int i,j, len=0, itrerations=0;
	len = strlen(str);
	for(i=0; i < len; i++){
		for(j=0; j+i+1 < len-j ; j++){
			itrerations++;
//			printf("len=%d,i=%d, j=%d, str[i]=%c, str[j+i+1]=%c, str[len-1-j]=%c\n", len, i, j, str[i], str[j+i+1], str[len-1-j]);
			if ( ( str[j+i+1] == str[i]) || (str[len-1-j] == str[i]) ){
				found_flag = 0;
				printf("Found a duplicate char (%c) @ %d itreration\n", str[i], itrerations);
				break; //change it to "return 0;" to exit after first match
			}
		}
	}
	return found_flag;
}

int determine_if_a_string(char *str)
{
	char *ch, *ch2;
	short found_flag = 1;
	int itrerations=0;
	for(ch = str; *ch != '\0'; ch++){
		for(ch2 = ch+1; *ch2 != '\0'; ch2++){
			itrerations++;
			if(*ch2 == *ch){
				found_flag = 0;
				printf("Found a duplicate char (%c) @ %d itreration\n", *ch, itrerations);
				break;  //change it to "return 0;" to exit after first match
			}
		}
	}
	return found_flag;
}

int main()
{
	char str[100];
	printf("Enter string: ");
	scanf("%s",str);
	
	printf("Using linear search:\n");
	if( determine_if_a_string(str) ){
		printf("'%s' is a unique string!!\n", str);
	}else{
		printf("'%s' not a unique string!\n");
	}

	printf("\nUsing dual search:\n");
	if( determine_if_a_string_2(str) ){
		printf("'%s' is a unique string!!\n", str);
	}else{
		printf("'%s' not a unique string!\n");
	}
		
}
/* Sample Output:

Enter string: SriRamJaiRamJaiJaiRam

Using linear search:
Found a duplicate char (i) @ 45 itreration
Found a duplicate char (R) @ 51 itreration
Found a duplicate char (a) @ 54 itreration
Found a duplicate char (m) @ 60 itreration
Found a duplicate char (J) @ 66 itreration
Found a duplicate char (a) @ 69 itreration
Found a duplicate char (i) @ 75 itreration
Found a duplicate char (R) @ 84 itreration
Found a duplicate char (a) @ 87 itreration
Found a duplicate char (m) @ 96 itreration
Found a duplicate char (J) @ 99 itreration
Found a duplicate char (a) @ 102 itreration
Found a duplicate char (i) @ 105 itreration
Found a duplicate char (a) @ 113 itreration
'SriRamJaiRamJaiJaiRam' not a unique string!

Using dual search:
Found a duplicate char (i) @ 24 itreration
Found a duplicate char (R) @ 27 itreration
Found a duplicate char (a) @ 29 itreration
Found a duplicate char (m) @ 30 itreration
Found a duplicate char (J) @ 36 itreration
Found a duplicate char (a) @ 38 itreration
Found a duplicate char (i) @ 42 itreration
Found a duplicate char (R) @ 45 itreration
Found a duplicate char (a) @ 47 itreration
Found a duplicate char (m) @ 48 itreration
Found a duplicate char (J) @ 51 itreration
Found a duplicate char (a) @ 53 itreration
Found a duplicate char (i) @ 56 itreration
Found a duplicate char (a) @ 61 itreration
'SriRamJaiRamJaiJaiRam' not a unique string!
 */
