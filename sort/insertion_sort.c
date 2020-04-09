#include <stdio.h>
#include "../utils/utils.h"

int main()
{
	int A[] = { 1,2,1,23,98,45,3,12,4 };
	int size = sizeof(A)/sizeof(A[0]);

	for (int j = 1; j < size; j++) {
		int key = A[j];
		int i = j - 1;
		while (i > -1 && A[i] > key) { // A[i] < key for descending
			A[i + 1] = A[i];
			i--;
		}
		A[i + 1] = key;
	}

	print_array(A, size);

	return 0;
}

