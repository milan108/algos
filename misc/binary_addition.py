
def main():
    A = [0,0,0,1]
    B = [1,1,1,1]
    print(add(A, B))


def add(A, B):
    n = len(A)
    C = [0 for _ in range(0, n + 1)]
    carry = 0
    for i in range(n - 1, -1, -1):
        C[i + 1] = (carry + A[i] + B[i]) % 2
        carry = 1 if (A[i] + B[i] + carry) > 1 else 0         
        
    C[0] = carry
    return C


if __name__ == '__main__':
    main()

