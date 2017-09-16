#include <stdio.h>
int main(){

	//double amp for logical 'and'
	// && will be True "if and only both are True"
	printf("Result of (1 && 0): %d\n", 1 && 0);	
	//double pipe for logical 'or'
	// || will be True if any one of them are true.
	printf("Result of (1 || 0): %d\n", 1 || 0);
/*	
	a & b 'bitwise and' # ignore for now
	&a	'address of ..' # use in scanf() and pointers
	a && b 'logical and'
*/ 
}
/*
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Result of (1 && 0): 0
Result of (1 || 0): 1
                        
*/
