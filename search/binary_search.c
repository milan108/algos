#include <stdio.h>

int binary_search(int[], int , int, int);

int main()
{
	int A[] = {0, 2, 13, 24, 35, 46, 57, 68};
	printf("%d\n", binary_search( A, 0 ,7, 57));
}

int binary_search (int A[], int left, int right, int n)
{
	int mid = (right - left) / 2;
	if (A[mid] == n) 
		return mid;
	n < A[mid] ? binary_search(A, 0, mid, n) : binary_search(A, mid + 1, right + 1, n);
}
