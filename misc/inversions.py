import sys

def merge(A, p, q, r):
    left, right = A[p:q + 1], A[q+1:r + 1]
    
    left.append(sys.maxsize)
    right.append(sys.maxsize)
   
    i,j = 0,0
    for k in range(p, r + 1):
        if left[i] >= right[j]:
            j += 1
        else:
            A[k] = left[i]
            i += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2 
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def m_merge(A, p, q, r):
    count = 0
    left, right = A[p:q + 1], A[q+1:r + 1]
    
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    
    i,j = 0,0
    while i < q - p + 1 and j < r - q:
        if left[i] > right[j]:
            count += 1
        j += 1
        if j == r - q:
            i += 1
            j = 0

    return count

def count_inversions(A, p, r):
    left, right, count = 0,0,0
    
    if p < r:
        q = (p + r) // 2
        count += count_inversions(A, p, q)
        count += count_inversions(A, q + 1, r)
        count += m_merge(A, p, q, r)
    
    return count

print(count_inversions([2,3,8,6,1], 0, 4))
print(count_inversions([2,3,8,6,1,0], 0, 5))
print(count_inversions([2,3,8,6,1,0,7,2], 0, 7))

"""
A = [2,3,8,6,1,0]
merge_sort(A, 0, len(A) - 1)
print(A)
"""
