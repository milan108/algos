#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

void print_array(int* A, int size)
{	
	for (int i = 0; i < size; i++) 
		printf("%d ", A[i]);

	printf("\n");
}

void swap(int* a, int* b)
{
	int tmp = *b;
	*b = *a;
	*a = tmp;
}

int* splice_array(int* original, int start, int end)
{
	original += start;
	
	int space = end - start + 1;
	
	int *subarray =  malloc(sizeof(int) * (space));
	if (!subarray)
		return NULL;
	for (int i = 0; i != space; i++) 
		subarray[i] = original[i];
	
	return subarray;
}

void reverse(char s[], int left, int right)
{
	if(right > left)
	{
		char tmp = s[left];
		s[left] = s[right];
		s[right] = tmp;
		reverse(s,++left,--right);
	}	
		
}
