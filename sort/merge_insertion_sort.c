#include <stdio.h>
#include <stdlib.h>
#include "../utils/utils.h"
#include <limits.h>

void merge(int*, int, int, int);
void merge_insertion_sort(int*, int, int, int);
void insertion_sort(int*, int, int);

// Show that insertion sort can sort n/k lists, each of length k, in theta(nk) worst case time. 

int main()
{
	int A[] = { 1,23,98,45,3,12,4,89,32,-3,-12,23,54,213,45,-9 };
	int size = sizeof(A)/sizeof(A[0]);
	merge_insertion_sort(A,0,size - 1 , 4);

	print_array(A, size);

	return 0;
}

void merge_insertion_sort(int* A, int p ,int r, int k)
{
	if (p < r) {
		int q = (r + p) / 2;
		if (r + p < k + 1) {
			insertion_sort(A,p,q);
			insertion_sort(A,q+1,r);
		} else {
			merge_insertion_sort(A, p, q, k);
			merge_insertion_sort(A, q + 1, r, k);
		}
		
		merge(A,p,q,r);
	}
}

void merge(int* A, int p, int q, int r)
{
	int n1 = q - p + 1;
	int n2 = r - q;

	int* L = (int*) malloc(sizeof(int) * n1);
	int* R = (int*) malloc(sizeof(int) * n2);

	int i, j;
	for (i = 0; i < n1; i++)
		L[i] = A[p + i]; 
	for (j = 0; j < n2; j++)
		R[j] = A[q + j + 1];
	
	i = 0;
	j = 0;

	L[n1] = INT_MAX;
	R[n2] = INT_MAX;

	for (int k = p; k < r + 1; k++)
	{	
		if (L[i] <= R[j]) {
			A[k] =L[i];
			i++;
		} else {
			A[k] = R[j];
			j++;
		} 
	}
}

void insertion_sort(int* A, int p, int q)
{
	int size = q - p + 1;
	for (int j = 1; j < size; j++) {
		int key = A[j];
		int i = j - 1;
		while (i > -1 && A[i] > key) {
			A[i + 1] = A[i];
			i--;
		}
		A[i + 1] = key;
	}
}
