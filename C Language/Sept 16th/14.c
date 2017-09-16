#include <stdio.h>
int main(){
	//double pipe for logical 'or'
	// || will be True "if any one of them" are true.
	// || will be False only if both are False.
	printf("Result of (0 || 0): %d\n", 0 || 0);
	printf("Result of (1 || 0): %d\n", 1 || 0);
	printf("Result of (0 || 1): %d\n", 0 || 1);
	printf("Result of (1 || 1): %d\n", 1 || 1);
}

/*
[2017-09-15 21:50.55]  /drives/d/W/Learning/0_C Lang
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Result of (0 || 0): 0
Result of (1 || 0): 1
Result of (0 || 1): 1
Result of (1 || 1): 1
*/
