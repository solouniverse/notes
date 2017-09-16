#include <stdio.h>
int main(){
/*
 * For every 4 year 
 * 	Ex: 2012,2016,2020....
 * Year should not be divisible by '100'
 * 	Ex: 100,200,300...2100 etc are "not" Leap years.
 * Year can be divisible by "400"
 * 	Ex: 1600, 2000, 2400 etc are Leap years.
 * 
*/
	int year=2200;
	//methodb - I
	if(year%4 == 0){
		if(year%100 == 0){
			if(year%400 == 0){
				printf("'%d' is a leap year!!\n", year);	
			}else{
				printf("'%d' is not a leap year\n", year);
			}
		}else{
			printf("'%d' is a leap year!!\n", year);	
		}
	}else{
		printf("'%d' is not a leap year\n", year);
	}
	//methodb - II
	if(year%400 == 0){
		printf("'%d' is a leap year!!\n", year);	
	}else{
		if(year%100 == 0){
			printf("'%d' is not a leap year\n", year);
		}else{
			if(year%4 == 0){
				printf("'%d' is a leap year!!\n", year);
			}else{
				printf("'%d' is not a leap year\n", year);
			}
		}
	}
	//methodb - III
	if(year%400 == 0){
		printf("'%d' is a leap year!!\n", year);	
	}else if(year%100 == 0){
			printf("'%d' is not a leap year\n", year);
	}else if(year%4 == 0){
		printf("'%d' is a leap year!!\n", year);
	}else{
		printf("'%d' is not a leap year\n", year);
	}
	//methodb - IV
	if( ( !(year%100 == 0) || (year%400 == 0)) && (year%4 == 0) ){
		printf("'%d' is a leap year!!\n", year);	
	}else{
		printf("'%d' is not a leap year\n", year);
	}
}
/*
[v-srm.MININT-7RKRDIO] ➤ ./a.exe
'2200' is not a leap year
'2200' is not a leap year
'2200' is not a leap year
'2200' is not a leap year
*/
