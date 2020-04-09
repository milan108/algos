#include<iostream>
#include<vector>

std::vector<int> addBinaries(std::vector<int>, std::vector<int>, std::vector<int>, int, int);
void printVector(std::vector<int>);

int main()
{
	//adds two binary arrays of the same length using recursion

	std::vector<int> A = { 1,0,1,1,0,0,1,1 };
	std::vector<int> B = { 1,0,1,1,1,1,0,0 };
	std::vector<int> C(A.size() + 1, 0);

	int i = A.size() - 1;
	int r = 0; // remainder

	printVector(addBinaries(A, B, C, i, r));

	return 0;
}

std::vector<int> addBinaries(std::vector<int> A, std::vector<int> B, std::vector<int> C, int i, int r) {
	if (i > -1) {
		C[i + 1] = A[i] + B[i] + r;
		if (C[i + 1] < 2) {
			r = 0;
		}
		else {
			(C[i + 1] == 2) ? C[i + 1] = 0 : C[i + 1] = 1;
			r = 1;
		}
		C[i] += r;
		i--;
		return addBinaries(A, B, C, i, r);

	}
	else {
		return C;
	}

}

void printVector(std::vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i];
		if (i == v.size() - 1) {
			std::cout << std::endl;
		}
	}
}
