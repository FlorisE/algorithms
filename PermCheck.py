# Check whether array A is a permutation.

def counting(A, m):
    count = [0] * m
    N = len(A)
    for i in range(N):
        count[A[i]-1] += 1
    return count

def solution(A):
    if max(A) > len(A):
        return 0
    count = counting(A, max(A))
    for c in count:
        if c == 0 or c > 1:
            return 0
    return 1

A = [0] * 4
A[0] = 4
A[1] = 1
A[2] = 3
A[3] = 2
# expected result: 1

A = [0] * 3
A[0] = 4
A[1] = 1
A[2] = 3
# expected result: 0
