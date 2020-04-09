#include <stdio.h>
#include <../utils/utils.h>

int main()
{
	int A[] = { 98,97,94,23,20,16,13,12,4,109,1 };
	size_t size = sizeof A / sizeof A[0];
	
	int placement_index = 0;

	while (placement_index < size - 1) {
		int min_index = placement_index;
		for (int i = placement_index; i < size; i++) {
			if (A[i] < A[placement_index]) {
				min_index = i;				
			} 
		}
		swap(&A[min_index], &A[placement_index]);
		placement_index++;
	}

	print_array(A, size);

	return 0;
}
