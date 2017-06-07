# Find the missing element in a given permutation.

def solution(A):
    N = len(A) + 1
    sN = N * (N + 1) / 2
    sA = sum(A)
    return sN - sA

A = [0] * 4
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5
# expected result: 4
