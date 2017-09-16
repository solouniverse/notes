#include <stdio.h>
int main(){
	// Below result will be same for all number not equal to zero in place of '1'
	printf("Result of (0 && 1 || 0): %d\n", 0 && 1 || 0);
	// && has higher priority over || 
	printf("Result of (0 && 1 || 1): %d\n", 0 && 1 || 1); 
	printf("Result of (0 && (1 || 1)): %d\n", 0 && (1 || 1)); 
	printf("Result of (1 || 1 && 0): %d\n", 1 || 1 && 0); 
	printf("Result of ((1 || 1) && 0): %d\n", (1 || 1) && 0); 
}
/*
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Result of (0 && 1 || 0): 0
Result of (0 && 1 || 1): 1
Result of (0 && (1 || 1)): 0
Result of (1 || 1 && 0): 1
Result of ((1 || 1) && 0): 0
*/
