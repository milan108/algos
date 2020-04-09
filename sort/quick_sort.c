#include "../utils/utils.h"
#include <stdio.h>
#include <stdlib.h>

void quicksort(int[], int, int);

int main() 
{
	int arr[] = {2,0,9,4,1,42,1,19};
	quicksort(arr, 0, 7);
	print_array(arr, 8);
	
	char s[] = "hello";
	reverse(s, 0, 4);
	printf("%s\n", s);
	return 0;
}

void quicksort(int v[], int left, int right) 
{
	int i, last;
	
	if(left >= right)
		return;
	
	swap(&v[left], &v[(left + right) / 2]);
	last = left;
	for (i = left + 1; i <= right; i++)
		if(v[i] < v[left])
			swap(&v[++last],&v[i]);
	swap(&v[left], &v[last]);
	quicksort(v, left, last - 1);
	quicksort(v, last + 1, right);
}


