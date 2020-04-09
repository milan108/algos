#include <stdio.h>
int main()
{
	//very simple yet it is a search algorithm
	int A[] = { 12,2,32,12,87,3,1,4 };
	int v = 3;
	size_t size = sizeof(A) / sizeof(A[0]);
	for (int i = 0; i < size; i++) {
		if (v == A[i]) {
			printf("%d\n",i);
			return i;
		}
	}

	return 0;
}

