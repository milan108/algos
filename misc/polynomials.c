#include <stdio.h>

int horners(int*, int, int);
int classic(int*, int, int);

int main() 
{
	int coeffs[] = {32, 0, 0, 0, 0, 1}; // least to most significant
	int n = sizeof(coeffs) / sizeof(coeffs[0]) - 1;
	int x = -2;

	printf("%d\n", horners(coeffs, n, x));
	printf("%d\n", classic(coeffs, n, x));

	return 0;	
}

int horners(int* coeffs, int n, int x)
{
	int y = 0;

	for(int i = n; i > -1; i--)	
		y = coeffs[i] + x * y;

	return y;
}

int classic(int* coeffs, int n, int x)
{
	int y = 0;

	for(int i = n; i > -1; i--)	
	{
		int yi = x;	
	
		for(int j = i; j > 0; j--)
			yi *= x
				;
		y += coeffs[i] * yi;	
	}

	return y;
}

