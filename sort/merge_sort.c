#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "../utils/utils.h"
#include "merge_sort.h"

void merge_sort(int* A, int p, int r) {
	if (p < r) {
		int q = (p + r) / 2;
		merge_sort(A, p, q);
		merge_sort(A, q + 1, r);
		merge(A, p, q, r);
	}
}

void merge(int* A, int p, int q, int r)
{
	int n1 = q - p + 1;
	int n2 = r - q;

	int* L = (int *) malloc(sizeof(int) * n1);
	int* R = (int *) malloc(sizeof(int) * n2);

	int i, j;
	for (i = 0; i < n1 ; i++)
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
		}
		else {
			A[k] = R[j];
			j++;
		} 
	}
}
 
