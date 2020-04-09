#include <stdio.h>
#include "../utils/utils.h"

int main()
{	
	int A[] = {123,23,4,32,12,21,3,45,2,3,231,32,12,32,123,213,321,1,2,3,1,11,35,1900,1234,1};
	int size =(int) sizeof(A)/sizeof(A[0]);
	
	for(int i = 0; i <  size - 1; i++) {
		for(int j = size - 1; j > i; j--) 
			if(A[j] < A[j - 1])
				swap(&A[j], &A[j-1]);
	}

	print_array(A, size);
	return 0;
}
