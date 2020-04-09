#include <stdio.h>
#include<string.h>
#include "../utils/utils.h"
#include "../sort/merge_sort.h"

#define 	TRUE	1
#define 	FALSE	0

int doesSumExist(int, int*, int);

int main()
{
	int S[] = {1,2,-8,7,9,-20,4,6};
	int x = 11;
	
	char answer[6] = "";
	doesSumExist(x,S,8) == TRUE ? strcpy(answer, "true"): strcpy(answer, "false");
	printf("%s\n", answer);

	return 0;
}
	
int doesSumExist(int x, int* S, int size)
{

	merge_sort(S, 0, size - 1);
	int i = 0 , j = size - 1;

	while (i < j){
		if(S[i] + S[j] == x){
			return TRUE;
		}
		if(S[i] + S[j] > x){
		 	j--;
		} 
		if(S[i] + S[j] < x){
			i++;
		}
	}
	
	return FALSE;
}
