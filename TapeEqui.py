# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

def solution(A):
    left = 0
    right = sum(A)
    N = len(A)
    minDiff = 100000
    for i in range(0,N-1):
        left += A[i]
        right -= A[i]
        summed = abs(left-right)
        if summed < minDiff:
            minDiff = summed
    return minDiff

A = [0] * 5
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 4
A[4] = 3
# expected result: 1
