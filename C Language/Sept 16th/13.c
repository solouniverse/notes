#include <stdio.h>
int main(){
//double amp for logical 'and'
// && will be True "if and only if both are True"
	printf("Result of (0 && 0): %d\n", 0 && 0);	
	printf("Result of (1 && 0): %d\n", 1 && 0);	
	printf("Result of (0 && 1): %d\n", 0 && 1);	
	printf("Result of (1 && 1): %d\n", 1 && 1);	
}
/*
[2017-09-15 21:47.55]  /drives/d/W/Learning/0_C Lang
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
Result of (0 && 0): 0
Result of (1 && 0): 0
Result of (0 && 1): 0
Result of (1 && 1): 1                
*/
